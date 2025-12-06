# 🚀 Como Configurar no Render.com (GRATUITO com Node.js)

## ✅ Por Que Render.com?

- ✅ Node.js **GRATUITO**
- ✅ MySQL **GRATUITO**
- ✅ HTTPS automático
- ✅ Deploy automático
- ✅ Muito fácil de usar

## 📋 Passo a Passo

### 1. Criar Conta no Render

1. Acesse: **https://render.com**
2. Clique em **"Get Started for Free"**
3. Faça login com **GitHub** (recomendado) ou email
4. Confirme seu email

### 2. Criar Web Service (Node.js)

1. No dashboard, clique em **"New +"**
2. Selecione **"Web Service"**
3. Conecte seu repositório GitHub (ou faça upload do código)

### 3. Configurar o Serviço

Preencha:

- **Name:** `keyauth-generator` (ou qualquer nome)
- **Region:** Escolha o mais próximo (ex: `Oregon`)
- **Branch:** `main` (ou `master`)
- **Root Directory:** (deixe vazio)
- **Runtime:** `Node`
- **Build Command:** `npm install`
- **Start Command:** `node server.js`
- **Instance Type:** `Free`

### 4. Configurar Variáveis de Ambiente

Na seção "Environment Variables", adicione:

```
NODE_ENV=production
PORT=10000
```

### 5. Criar Banco MySQL

1. No dashboard, clique em **"New +"**
2. Selecione **"PostgreSQL"** (ou MySQL se disponível)
3. Escolha **"Free"**
4. Anote as credenciais:
   - Host
   - Database
   - User
   - Password
   - Port

### 6. Atualizar Configuração do Banco

Edite `config/database.js` com as credenciais do Render:

```javascript
const dbConfig = {
  host: 'seu-host-do-render',
  user: 'seu-usuario',
  password: 'sua-senha',
  database: 'seu-database',
  // ...
};
```

### 7. Deploy

1. Clique em **"Create Web Service"**
2. Aguarde o deploy (pode demorar alguns minutos)
3. Quando terminar, você terá uma URL: `https://keyauth-generator.onrender.com`

### 8. Testar

Acesse:
```
https://sua-url.onrender.com/api/health
```

Deve retornar JSON válido!

## ✅ Pronto!

Agora você tem Node.js funcionando de graça!

---

**💡 Dica:** O Render.com é muito mais fácil que configurar Node.js no InfinityFree, e é totalmente gratuito!

