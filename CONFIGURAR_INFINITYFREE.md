# ⚙️ Configurar Node.js no InfinityFree - Passo a Passo

## ❌ Problema: Erro 404 em todas as rotas `/api/*`

Se você está recebendo `errors.infinityfree.net/errors/404/`, significa que o **Node.js não está processando as requisições**.

## ✅ Solução Completa

### Passo 1: Verificar Arquivos Enviados

Certifique-se de que estes arquivos estão na **raiz** do seu site (htdocs/):

- ✅ `index.html`
- ✅ `server.js`
- ✅ `package.json`
- ✅ `.htaccess` (novo arquivo criado)
- ✅ `config/database.js`
- ✅ `css/styles.css`
- ✅ `js/script.js`

### Passo 2: Configurar Node.js no Painel

1. **Acesse o painel do InfinityFree**
2. **Vá em "Node.js"** (menu lateral esquerdo)
3. **Selecione seu domínio**
4. **Configure:**

   ```
   Startup File: server.js
   Node.js Version: 18.x (ou superior)
   ```

5. **Clique em "Save"**

### Passo 3: Iniciar o Servidor

1. No painel Node.js, verifique o **status**
2. Se estiver **"Stopped"**, clique em **"Start"**
3. Aguarde alguns segundos
4. O status deve mudar para **"Running"**

### Passo 4: Verificar Logs

1. No painel Node.js, clique em **"View Logs"**
2. Procure por estas mensagens:

   ✅ **Sucesso:**
   ```
   🔄 Testando conexão com MySQL...
   ✅ Conexão com MySQL estabelecida com sucesso!
   ✅ Tabela "keys" verificada/criada com sucesso!
   🚀 Servidor KeyAuth rodando em http://localhost:XXXX
   ```

   ❌ **Erro:**
   ```
   ❌ Erro ao conectar com MySQL: ...
   ❌ Não foi possível conectar ao banco de dados
   ```

### Passo 5: Testar

1. **Teste a API diretamente:**
   ```
   https://seudominio.com/api/health
   ```
   
   **Deve retornar:**
   ```json
   {
     "status": "ok",
     "message": "API está funcionando",
     "timestamp": "...",
     "server": "Node.js/Express",
     "database": "MySQL"
   }
   ```

2. **Teste a página de diagnóstico:**
   ```
   https://seudominio.com/test
   ```

3. **Teste a rota simples:**
   ```
   https://seudominio.com/api/test
   ```

## 🔧 Problemas Comuns

### Problema 1: "App não inicia"

**Causa:** Erro no código ou dependências não instaladas.

**Solução:**
1. Verifique os logs no painel
2. Verifique se `package.json` está correto
3. O InfinityFree instala dependências automaticamente, mas pode demorar

### Problema 2: "Erro de conexão MySQL"

**Causa:** Credenciais incorretas ou banco não existe.

**Solução:**
1. Verifique `config/database.js`
2. Verifique se o banco existe no painel MySQL
3. Verifique as credenciais no painel

### Problema 3: "Porta já em uso"

**Causa:** Outro processo usando a porta.

**Solução:**
1. No InfinityFree, geralmente é automático
2. Não precisa configurar porta manualmente
3. Se houver erro, verifique os logs

### Problema 4: "404 em todas as rotas"

**Causa:** Node.js não está rodando ou não está configurado.

**Solução:**
1. ✅ Verifique se está "Running" no painel
2. ✅ Verifique se Startup File = `server.js`
3. ✅ Verifique os logs
4. ✅ Teste `/api/health` diretamente

## 📋 Checklist Final

Antes de testar, verifique:

- [ ] Todos os arquivos foram enviados
- [ ] `server.js` está na raiz
- [ ] `package.json` está na raiz
- [ ] `.htaccess` está na raiz
- [ ] Node.js está configurado no painel
- [ ] Startup File = `server.js`
- [ ] Status = "Running"
- [ ] Logs não mostram erros críticos
- [ ] `/api/health` retorna JSON válido

## 🆘 Ainda Não Funciona?

1. **Verifique os logs** - Sempre comece aqui!
2. **Teste `/api/health`** - Se não funcionar, o Node.js não está rodando
3. **Verifique se o app está "Running"** - Se não estiver, inicie
4. **Verifique o Startup File** - Deve ser exatamente `server.js`
5. **Aguarde alguns minutos** - Às vezes o InfinityFree demora para iniciar

## 📝 Notas Importantes

- O InfinityFree pode demorar alguns minutos para iniciar o Node.js
- Os logs são atualizados em tempo real
- Se mudar arquivos, pode precisar reiniciar o app
- A porta é automática, não precisa configurar

## ✅ Quando Estiver Funcionando

Você verá:
- ✅ `/api/health` retorna JSON
- ✅ `/api/stats` retorna estatísticas
- ✅ Interface carrega sem erros 404
- ✅ Consegue gerar keys
- ✅ Logs mostram requisições sendo processadas

