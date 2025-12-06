# 🔍 Como Verificar se o Servidor Está Rodando

## ❌ Erro: HTTP 404

Se você está recebendo erro 404, significa que o servidor Node.js **não está rodando** ou não está configurado corretamente.

## ✅ Passo a Passo para Resolver

### 1. Verificar no Painel InfinityFree

1. **Acesse o painel do InfinityFree**
2. **Vá em "Node.js"** (no menu lateral)
3. **Verifique o status:**
   - ✅ Se estiver **"Running"** → O servidor está rodando
   - ❌ Se estiver **"Stopped"** → Clique em **"Start"**

### 2. Verificar Configuração

No painel Node.js, verifique:

- **Startup File:** Deve ser `server.js`
- **Node.js Version:** 18.x ou superior
- **Port:** Geralmente automático (não precisa configurar)

### 3. Verificar Logs

1. No painel Node.js, clique em **"View Logs"**
2. Procure por:
   - ✅ `Servidor KeyAuth rodando em...` → Está funcionando!
   - ❌ Erros de MySQL → Problema de conexão com banco
   - ❌ Erros de porta → Porta já em uso

### 4. Testar a API

Abra no navegador:
```
https://seudominio.com/api/health
```

**Deve retornar:**
```json
{
  "status": "ok",
  "message": "API está funcionando",
  "timestamp": "2024-..."
}
```

**Se retornar 404:**
- O servidor Node.js não está rodando
- Siga os passos acima

### 5. Página de Teste

Acesse:
```
https://seudominio.com/test
```

Esta página testa automaticamente a conexão com a API e mostra o status.

## 🔧 Problemas Comuns

### Problema: "App não inicia"

**Solução:**
1. Verifique se `server.js` existe na raiz
2. Verifique se `package.json` existe
3. Verifique os logs para erros
4. Tente reinstalar dependências

### Problema: "Erro de conexão MySQL"

**Solução:**
1. Verifique `config/database.js`
2. Verifique se o banco de dados existe
3. Verifique as credenciais no painel MySQL do InfinityFree

### Problema: "Porta já em uso"

**Solução:**
1. No InfinityFree, geralmente a porta é automática
2. Não precisa configurar manualmente
3. Se houver erro, verifique os logs

## 📋 Checklist Rápido

- [ ] Node.js está **Running** no painel
- [ ] Startup File = `server.js`
- [ ] `server.js` existe na raiz
- [ ] `package.json` existe na raiz
- [ ] `config/database.js` existe
- [ ] Logs não mostram erros críticos
- [ ] `/api/health` retorna JSON válido

## 🆘 Ainda com Problemas?

1. **Verifique os logs** no painel Node.js
2. **Teste a API** diretamente: `/api/health`
3. **Use a página de teste**: `/test`
4. **Verifique se todos os arquivos foram enviados**

## 📝 Comandos Úteis (se tiver acesso SSH)

```bash
# Verificar se o processo está rodando
ps aux | grep node

# Ver logs em tempo real
tail -f logs/app.log

# Reiniciar o app
# (Faça pelo painel do InfinityFree)
```

