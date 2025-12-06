# 🔧 Solução de Erros - KeyAuth InfinityFree

## ❌ Erros Comuns e Soluções

### Erro 404 - API não encontrada

**Sintomas:**
```
Failed to load resource: the server responded with a status of 404
SyntaxError: Unexpected non-whitespace character after JSON
```

**Causa:** O servidor Node.js não está rodando ou as rotas não estão configuradas.

**Solução:**

1. **Verificar se o Node.js está rodando no InfinityFree:**
   - Acesse o painel do InfinityFree
   - Vá em **Node.js**
   - Verifique se o app está **Running**
   - Se não estiver, clique em **Start**

2. **Verificar configuração do Node.js:**
   - **Startup File:** deve ser `server.js`
   - **Node.js Version:** 18.x ou superior

3. **Verificar logs:**
   - No painel Node.js, veja os logs
   - Procure por erros de conexão MySQL
   - Verifique se a porta está correta

### Erro de Conexão MySQL

**Sintomas:**
```
Erro ao conectar com MySQL
```

**Solução:**
1. Verifique `config/database.js`:
   - Host: `sql305.infinityfree.com`
   - Database: `if0_40460911_keyauth`
   - User: `if0_40460911`
   - Password: `zlshop12345`

2. Verifique se o banco de dados existe no InfinityFree

3. A tabela será criada automaticamente na primeira execução

### Erro: Resposta não é JSON

**Sintomas:**
```
SyntaxError: Unexpected non-whitespace character after JSON
```

**Causa:** O servidor está retornando HTML (página de erro) ao invés de JSON.

**Solução:**
1. Verifique se o servidor Node.js está rodando
2. Verifique se as rotas `/api/*` estão funcionando
3. Teste diretamente: `https://seudominio.com/api/stats`

### Como Testar se a API Está Funcionando

1. **No navegador:**
   ```
   https://seudominio.com/api/stats
   ```
   Deve retornar JSON:
   ```json
   {"stats":{"total":0,"active":0,"inactive":0,"expired":0,"programs":0}}
   ```

2. **Com o script Python:**
   ```python
   # Edite test_keyauth.py e altere:
   API_URL = "https://seudominio.com"
   
   # Execute:
   python test_keyauth.py
   ```

## ✅ Checklist de Verificação

Antes de reportar erros, verifique:

- [ ] Node.js está rodando no painel InfinityFree
- [ ] Startup File está configurado como `server.js`
- [ ] Porta está correta (geralmente automática no InfinityFree)
- [ ] Banco de dados MySQL existe e está acessível
- [ ] Arquivos foram enviados corretamente:
  - [ ] `index.html` na raiz
  - [ ] `server.js` na raiz
  - [ ] `package.json` na raiz
  - [ ] `config/database.js` existe
  - [ ] `css/styles.css` existe
  - [ ] `js/script.js` existe

## 🔍 Debug

### Ver logs do servidor:
1. Painel InfinityFree → Node.js
2. Clique em **View Logs**
3. Procure por erros

### Testar API manualmente:
```bash
# No terminal (ou Postman):
curl https://seudominio.com/api/stats

# Deve retornar JSON válido
```

### Verificar se arquivos estão corretos:
```bash
# Verifique se os arquivos existem:
ls -la index.html
ls -la server.js
ls -la config/database.js
```

## 📞 Próximos Passos

Se ainda tiver problemas:

1. Verifique os logs do Node.js no InfinityFree
2. Teste a API diretamente no navegador
3. Verifique se todas as dependências foram instaladas
4. Certifique-se de que o banco de dados está acessível

