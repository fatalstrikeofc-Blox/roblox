const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const { v4: uuidv4 } = require('uuid');
const { pool, testConnection, initializeDatabase } = require('./config/database');

const app = express();
// Porta do InfinityFree (usa variável de ambiente ou padrão 3000)
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Log de todas as requisições (para debug)
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`);
    next();
});

// Servir arquivos estáticos da raiz (para InfinityFree)
app.use(express.static('.'));
app.use('/css', express.static('css'));
app.use('/js', express.static('js'));

// Rota para servir index.html na raiz
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Rota de teste/health check
app.get('/test', (req, res) => {
    res.sendFile(__dirname + '/test.html');
});

// Rota de health check da API (deve ser acessível)
app.get('/api/health', (req, res) => {
    res.json({ 
        status: 'ok', 
        message: 'API está funcionando',
        timestamp: new Date().toISOString(),
        server: 'Node.js/Express',
        database: 'MySQL'
    });
});

// Rota de teste simples
app.get('/api/test', (req, res) => {
    res.json({ 
        success: true,
        message: 'API Node.js está respondendo!',
        path: req.path,
        method: req.method
    });
});

// Função para gerar uma key única
function generateKey() {
  const randomBytes = crypto.randomBytes(16);
  const key = randomBytes.toString('hex').toUpperCase();
  return `${key.substring(0, 8)}-${key.substring(8, 16)}-${key.substring(16, 24)}-${key.substring(24, 32)}`;
}

// Converter resultado do MySQL para objeto
function mysqlToObject(row) {
  return {
    id: row.id,
    key: row.key_value,
    program: row.program,
    createdAt: row.created_at ? new Date(row.created_at).toISOString() : null,
    expiresAt: row.expires_at ? new Date(row.expires_at).toISOString() : null,
    days: row.days,
    notes: row.notes || '',
    isActive: row.is_active === 1 || row.is_active === true,
    usedAt: row.used_at ? new Date(row.used_at).toISOString() : null,
    lastValidated: row.last_validated ? new Date(row.last_validated).toISOString() : null,
    validationCount: row.validation_count || 0
  };
}

// Rotas da API

// Gerar nova key
app.post('/api/generate', async (req, res) => {
  try {
    const { program, days, notes } = req.body;
    
    if (!program) {
      return res.status(400).json({ error: 'Nome do programa é obrigatório' });
    }

    const key = generateKey();
    const expirationDate = days ? new Date(Date.now() + days * 24 * 60 * 60 * 1000) : null;
    const keyId = uuidv4();
    const now = new Date();

    const [result] = await pool.execute(
      `INSERT INTO keys (id, key_value, program, created_at, expires_at, days, notes, is_active, validation_count)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      [keyId, key, program, now, expirationDate, days || null, notes || '', true, 0]
    );

    const keyData = {
      id: keyId,
      key: key,
      program: program,
      createdAt: now.toISOString(),
      expiresAt: expirationDate ? expirationDate.toISOString() : null,
      days: days || null,
      notes: notes || '',
      isActive: true,
      usedAt: null,
      lastValidated: null,
      validationCount: 0
    };

    res.json({ success: true, key: keyData });
  } catch (error) {
    console.error('Erro ao gerar key:', error);
    if (error.code === 'ER_DUP_ENTRY') {
      return res.status(400).json({ error: 'Key duplicada, tente novamente' });
    }
    res.status(500).json({ error: 'Erro ao gerar key' });
  }
});

// Validar key
app.post('/api/validate', async (req, res) => {
  try {
    const { key, program } = req.body;

    if (!key || !program) {
      return res.status(400).json({ error: 'Key e programa são obrigatórios' });
    }

    const [rows] = await pool.execute(
      `SELECT * FROM keys WHERE key_value = ? AND program = ?`,
      [key, program]
    );

    if (rows.length === 0) {
      return res.json({ valid: false, message: 'Key inválida ou não encontrada' });
    }

    const keyData = mysqlToObject(rows[0]);

    if (!keyData.isActive) {
      return res.json({ valid: false, message: 'Key desativada' });
    }

    // Verificar expiração
    if (keyData.expiresAt) {
      const expirationDate = new Date(keyData.expiresAt);
      if (new Date() > expirationDate) {
        return res.json({ valid: false, message: 'Key expirada' });
      }
    }

    // Atualizar estatísticas
    const now = new Date();
    const usedAt = keyData.usedAt ? keyData.usedAt : now.toISOString();
    
    await pool.execute(
      `UPDATE keys 
       SET last_validated = ?, validation_count = validation_count + 1, used_at = COALESCE(used_at, ?)
       WHERE id = ?`,
      [now, usedAt, keyData.id]
    );

    const daysRemaining = keyData.expiresAt 
      ? Math.ceil((new Date(keyData.expiresAt) - new Date()) / (1000 * 60 * 60 * 24))
      : null;

    res.json({ 
      valid: true, 
      message: 'Key válida',
      expiresAt: keyData.expiresAt,
      daysRemaining: daysRemaining
    });
  } catch (error) {
    console.error('Erro ao validar key:', error);
    res.status(500).json({ error: 'Erro ao validar key' });
  }
});

// Listar todas as keys
app.get('/api/keys', async (req, res) => {
  try {
    const [rows] = await pool.execute(
      `SELECT * FROM keys ORDER BY created_at DESC`
    );
    
    const keys = rows.map(row => mysqlToObject(row));
    res.json({ keys });
  } catch (error) {
    console.error('Erro ao listar keys:', error);
    res.status(500).json({ error: 'Erro ao listar keys' });
  }
});

// Obter key específica
app.get('/api/keys/:id', async (req, res) => {
  try {
    const [rows] = await pool.execute(
      `SELECT * FROM keys WHERE id = ?`,
      [req.params.id]
    );
    
    if (rows.length === 0) {
      return res.status(404).json({ error: 'Key não encontrada' });
    }

    const key = mysqlToObject(rows[0]);
    res.json({ key });
  } catch (error) {
    console.error('Erro ao obter key:', error);
    res.status(500).json({ error: 'Erro ao obter key' });
  }
});

// Atualizar key (ativar/desativar)
app.put('/api/keys/:id', async (req, res) => {
  try {
    const { isActive, notes } = req.body;
    
    let updateQuery = 'UPDATE keys SET ';
    const updateValues = [];
    
    if (typeof isActive === 'boolean') {
      updateQuery += 'is_active = ?, ';
      updateValues.push(isActive);
    }
    
    if (notes !== undefined) {
      updateQuery += 'notes = ?, ';
      updateValues.push(notes);
    }
    
    // Remover última vírgula e espaço
    updateQuery = updateQuery.slice(0, -2);
    updateQuery += ' WHERE id = ?';
    updateValues.push(req.params.id);
    
    const [result] = await pool.execute(updateQuery, updateValues);
    
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'Key não encontrada' });
    }
    
    // Buscar key atualizada
    const [rows] = await pool.execute(
      `SELECT * FROM keys WHERE id = ?`,
      [req.params.id]
    );
    
    const key = mysqlToObject(rows[0]);
    res.json({ success: true, key });
  } catch (error) {
    console.error('Erro ao atualizar key:', error);
    res.status(500).json({ error: 'Erro ao atualizar key' });
  }
});

// Deletar key
app.delete('/api/keys/:id', async (req, res) => {
  try {
    const [result] = await pool.execute(
      `DELETE FROM keys WHERE id = ?`,
      [req.params.id]
    );
    
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'Key não encontrada' });
    }
    
    res.json({ success: true });
  } catch (error) {
    console.error('Erro ao deletar key:', error);
    res.status(500).json({ error: 'Erro ao deletar key' });
  }
});

// Estatísticas
app.get('/api/stats', async (req, res) => {
  try {
    const [rows] = await pool.execute(`SELECT * FROM keys`);
    const keys = rows.map(row => mysqlToObject(row));
    
    const stats = {
      total: keys.length,
      active: keys.filter(k => k.isActive).length,
      inactive: keys.filter(k => !k.isActive).length,
      expired: keys.filter(k => k.expiresAt && new Date(k.expiresAt) < new Date()).length,
      programs: [...new Set(keys.map(k => k.program))].length
    };

    res.json({ stats });
  } catch (error) {
    console.error('Erro ao obter estatísticas:', error);
    res.status(500).json({ error: 'Erro ao obter estatísticas' });
  }
});

// Inicializar servidor
async function startServer() {
  console.log('🔄 Testando conexão com MySQL...');
  const connected = await testConnection();
  
  if (!connected) {
    console.error('❌ Não foi possível conectar ao banco de dados. Verifique as configurações.');
    process.exit(1);
  }
  
  console.log('🔄 Inicializando banco de dados...');
  await initializeDatabase();
  
  app.listen(PORT, () => {
    console.log(`🚀 Servidor KeyAuth rodando em http://localhost:${PORT}`);
    console.log(`📊 Interface disponível em http://localhost:${PORT}`);
    console.log(`💾 Banco de dados: MySQL (InfinityFree)`);
  });
}

startServer();
