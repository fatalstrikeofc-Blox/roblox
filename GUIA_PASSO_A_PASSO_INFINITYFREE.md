# 📖 Guia Passo a Passo - Configurar Node.js no InfinityFree

## ⚠️ IMPORTANTE: Verificar se Você Tem Node.js

**O plano GRATUITO do InfinityFree NÃO inclui Node.js!**

Antes de começar, verifique:
- ✅ Se você tem um plano **PAGO** do InfinityFree → Tem Node.js
- ❌ Se você tem plano **GRATUITO** → NÃO tem Node.js

## 🔍 Passo 1: Acessar o Painel do InfinityFree

1. **Acesse:** https://infinityfree.net
2. **Faça login** na sua conta
3. Você será redirecionado para o **painel de controle**

## 🔍 Passo 2: Verificar se Você Vê "Node.js" no Menu

No menu lateral esquerdo, procure por:

### ✅ Se você VÊ "Node.js":
- Continue com os próximos passos
- Você tem acesso ao Node.js

### ❌ Se você NÃO VÊ "Node.js":
- Você **NÃO tem Node.js** disponível
- O plano gratuito não inclui Node.js
- Veja o arquivo `ALTERNATIVAS.md` para outras opções

## 📋 Passo 3: Acessar a Seção Node.js

1. No menu lateral esquerdo, clique em **"Node.js"**
2. Você verá uma lista dos seus domínios/sites

## 📋 Passo 4: Selecionar Seu Domínio

1. Na lista, encontre o domínio onde você quer configurar o Node.js
2. Clique no **nome do domínio** ou no botão **"Manage"** (Gerenciar)

## ⚙️ Passo 5: Configurar o Node.js

Você verá uma página de configuração com os seguintes campos:

### Campos a Preencher:

1. **Startup File (Arquivo de Inicialização):**
   ```
   server.js
   ```
   ⚠️ **IMPORTANTE:** Deve ser exatamente `server.js` (sem caminho, sem barras)

2. **Node.js Version (Versão do Node.js):**
   - Selecione: **18.x** ou **20.x** (qualquer versão 18 ou superior)
   - Geralmente há opções como: `18.17.0`, `20.9.0`, etc.

3. **Environment Variables (Variáveis de Ambiente):** (Opcional)
   - Deixe vazio por enquanto
   - Não precisa configurar nada aqui

### Exemplo de Configuração:

```
Startup File: server.js
Node.js Version: 18.17.0 (ou 20.x)
Environment Variables: (vazio)
```

## 💾 Passo 6: Salvar a Configuração

1. Após preencher os campos, role a página para baixo
2. Clique no botão **"Save"** (Salvar) ou **"Update"** (Atualizar)
3. Aguarde a confirmação de que foi salvo

## ▶️ Passo 7: Iniciar o Servidor Node.js

1. Na mesma página, procure pelo **status do servidor**
2. Você verá algo como:
   - **Status: Stopped** (Parado) ❌
   - **Status: Running** (Rodando) ✅

3. **Se estiver "Stopped":**
   - Clique no botão **"Start"** (Iniciar)
   - Aguarde alguns segundos
   - O status deve mudar para **"Running"**

4. **Se já estiver "Running":**
   - Tudo certo! O servidor já está rodando
   - Se não estiver funcionando, tente clicar em **"Restart"** (Reiniciar)

## 📊 Passo 8: Verificar os Logs

1. Na mesma página, procure por **"View Logs"** ou **"Logs"**
2. Clique para ver os logs do servidor
3. Procure por estas mensagens:

### ✅ Mensagens de Sucesso:
```
🔄 Testando conexão com MySQL...
✅ Conexão com MySQL estabelecida com sucesso!
✅ Tabela "keys" verificada/criada com sucesso!
🚀 Servidor KeyAuth rodando em http://localhost:XXXX
```

### ❌ Mensagens de Erro:
```
❌ Erro ao conectar com MySQL: ...
❌ Não foi possível conectar ao banco de dados
```

## ✅ Passo 9: Testar se Está Funcionando

1. Abra uma nova aba no navegador
2. Acesse: `https://seudominio.com/api/health`
3. **Deve retornar JSON:**
   ```json
   {
     "status": "ok",
     "message": "API está funcionando",
     "timestamp": "..."
   }
   ```

4. **Se retornar 404:**
   - O servidor ainda não está rodando
   - Volte ao Passo 7 e verifique o status
   - Verifique os logs para erros

## 🔧 Problemas Comuns e Soluções

### Problema 1: Não Vejo "Node.js" no Menu

**Causa:** Você não tem Node.js disponível (plano gratuito)

**Solução:**
- Use Render.com (gratuito com Node.js)
- Ou peça para eu criar versão PHP

### Problema 2: Erro ao Salvar Configuração

**Causa:** Arquivo `server.js` não existe ou está no lugar errado

**Solução:**
1. Verifique se `server.js` está na **raiz** do seu site
2. Verifique se o nome está correto: `server.js` (não `Server.js` ou `server.JS`)
3. Faça upload do arquivo se necessário

### Problema 3: Status Fica "Stopped" ou Não Inicia

**Causa:** Erro no código ou dependências não instaladas

**Solução:**
1. Verifique os **logs** para ver o erro específico
2. Verifique se `package.json` existe na raiz
3. O InfinityFree instala dependências automaticamente, mas pode demorar

### Problema 4: Erro de Conexão MySQL

**Causa:** Credenciais incorretas ou banco não existe

**Solução:**
1. Verifique `config/database.js`
2. Verifique se o banco existe no painel MySQL
3. Verifique as credenciais no painel MySQL

## 📝 Checklist Final

Antes de testar, verifique:

- [ ] Você tem acesso ao Node.js (não é plano gratuito)
- [ ] `server.js` está na raiz do site
- [ ] `package.json` está na raiz do site
- [ ] `config/database.js` existe
- [ ] Startup File = `server.js`
- [ ] Node.js Version = 18.x ou 20.x
- [ ] Status = "Running"
- [ ] Logs não mostram erros críticos
- [ ] `/api/health` retorna JSON válido

## 🆘 Ainda Não Funciona?

1. **Verifique os logs** - Sempre comece aqui!
2. **Teste `/api/health`** - Se não funcionar, o Node.js não está rodando
3. **Verifique se o app está "Running"** - Se não estiver, inicie
4. **Verifique o Startup File** - Deve ser exatamente `server.js`
5. **Aguarde alguns minutos** - Às vezes demora para iniciar

## 📞 Próximos Passos

Se você **NÃO tem Node.js** no InfinityFree:

1. Veja o arquivo `ALTERNATIVAS.md`
2. Use Render.com (recomendado)
3. Ou peça para eu criar versão PHP

---

**💡 Dica:** Se você não tem Node.js no InfinityFree, o melhor é usar Render.com. É gratuito e muito mais fácil de configurar!

