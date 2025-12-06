# 🌐 Guia de Upload para InfinityFree

## 📁 Estrutura de Arquivos para Upload

### Arquivos Obrigatórios na Raiz:
```
/
├── index.html          ✅ OBRIGATÓRIO - Arquivo principal
├── server.js           ✅ Servidor Node.js
├── package.json        ✅ Dependências
└── .htaccess          (opcional - se necessário)
```

### Pastas:
```
/
├── css/
│   └── styles.css     ✅ Estilos
├── js/
│   └── script.js      ✅ JavaScript
├── config/
│   └── database.js    ✅ Configuração MySQL
└── exemplos/          (opcional - apenas para referência)
```

## 📤 Passo a Passo para Upload

### 1. Preparar Arquivos

Certifique-se de que você tem:
- ✅ `index.html` na raiz
- ✅ `css/styles.css`
- ✅ `js/script.js`
- ✅ `server.js`
- ✅ `package.json`
- ✅ `config/database.js`

### 2. Upload via File Manager (InfinityFree)

1. Acesse o **File Manager** no painel do InfinityFree
2. Navegue até a pasta `htdocs` (ou pasta raiz do seu site)
3. Faça upload dos arquivos na seguinte ordem:

#### Primeiro: Criar Pastas
- Criar pasta `css/`
- Criar pasta `js/`
- Criar pasta `config/`

#### Segundo: Upload dos Arquivos
- Upload `index.html` → **raiz** (htdocs/)
- Upload `styles.css` → **css/**
- Upload `script.js` → **js/**
- Upload `server.js` → **raiz**
- Upload `package.json` → **raiz**
- Upload `database.js` → **config/**

### 3. Configurar Node.js no InfinityFree

1. No painel do InfinityFree, vá em **Node.js**
2. Selecione seu domínio
3. Configure:
   - **Startup File:** `server.js`
   - **Node.js Version:** 18.x ou superior
4. Clique em **Save**

### 4. Instalar Dependências

No terminal SSH do InfinityFree (se disponível) ou via Node.js App:

```bash
npm install
```

Ou o InfinityFree pode instalar automaticamente ao detectar o `package.json`.

### 5. Verificar Configuração do Banco

O arquivo `config/database.js` já está configurado com suas credenciais:
- Host: sql305.infinityfree.com
- Database: if0_40460911_keyauth
- User: if0_40460911
- Password: zlshop12345

**A tabela será criada automaticamente na primeira execução!**

### 6. Testar

1. Acesse seu site: `https://seudominio.com`
2. O `index.html` deve carregar automaticamente
3. Teste gerar uma key
4. Execute o script Python de teste localmente para validar a API

## ⚠️ Importante

### Permissões de Arquivo
- Certifique-se de que os arquivos têm permissões de leitura
- O `server.js` precisa de permissão de execução

### Porta do Servidor
- O InfinityFree pode usar uma porta diferente
- Verifique nas configurações do Node.js qual porta está sendo usada
- Se necessário, ajuste a variável `PORT` no `server.js`

### Variáveis de Ambiente (se necessário)
Se o InfinityFree usar variáveis de ambiente, você pode criar um arquivo `.env`:
```
DB_HOST=sql305.infinityfree.com
DB_USER=if0_40460911
DB_PASS=zlshop12345
DB_NAME=if0_40460911_keyauth
```

## 🔧 Troubleshooting

### Problema: index.html não carrega
- ✅ Verifique se está na raiz (htdocs/)
- ✅ Verifique permissões do arquivo
- ✅ Limpe o cache do navegador

### Problema: CSS/JS não carregam
- ✅ Verifique os caminhos em `index.html`:
  - `css/styles.css` ✅
  - `js/script.js` ✅
- ✅ Verifique se os arquivos estão nas pastas corretas
- ✅ Verifique permissões das pastas

### Problema: API não funciona
- ✅ Verifique se o Node.js está rodando
- ✅ Verifique os logs do servidor
- ✅ Verifique a conexão com MySQL
- ✅ Teste a API diretamente: `https://seudominio.com/api/stats`

### Problema: Erro de conexão MySQL
- ✅ Verifique as credenciais em `config/database.js`
- ✅ Verifique se o banco de dados existe
- ✅ Verifique se o host MySQL está acessível

## 📝 Checklist Final

Antes de fazer upload, verifique:

- [ ] `index.html` está na raiz
- [ ] `css/styles.css` existe e está em `css/`
- [ ] `js/script.js` existe e está em `js/`
- [ ] `server.js` está na raiz
- [ ] `package.json` está na raiz
- [ ] `config/database.js` existe e tem as credenciais corretas
- [ ] Caminhos em `index.html` estão corretos:
  - `<link rel="stylesheet" href="css/styles.css">`
  - `<script src="js/script.js"></script>`

## 🎉 Pronto!

Após o upload, seu site KeyAuth estará funcionando no InfinityFree!

