# 🎯 Como Acessar Node.js no InfinityFree - Guia Visual

## 📍 Localização no Painel

### Passo 1: Login
1. Acesse: **https://infinityfree.net**
2. Clique em **"Login"** (canto superior direito)
3. Digite seu email e senha
4. Clique em **"Login"**

### Passo 2: Menu Lateral

Após fazer login, você verá o **painel de controle** com um **menu lateral esquerdo**.

O menu tem estas opções:
```
🏠 Dashboard
📁 File Manager
🌐 Domains
💾 MySQL Databases
📊 Statistics
⚙️ Node.js  ← PROCURE ESTA OPÇÃO
🔧 Settings
...
```

### Passo 3: Clicar em Node.js

1. No menu lateral esquerdo, procure por **"Node.js"**
2. Clique em **"Node.js"**

**⚠️ IMPORTANTE:**
- Se você **VÊ** "Node.js" → Continue
- Se você **NÃO VÊ** "Node.js" → Você não tem acesso (plano gratuito)

## 🖼️ O Que Você Verá

### Tela Inicial do Node.js

Após clicar em "Node.js", você verá:

```
┌─────────────────────────────────────────┐
│  Node.js Applications                   │
├─────────────────────────────────────────┤
│                                         │
│  Domain: seudominio.com                 │
│  Status: Stopped                        │
│  [Manage] [Start]                       │
│                                         │
└─────────────────────────────────────────┘
```

### Tela de Configuração

Ao clicar em **"Manage"**, você verá:

```
┌─────────────────────────────────────────┐
│  Node.js Configuration                  │
├─────────────────────────────────────────┤
│                                         │
│  Startup File: [server.js        ]     │
│                                         │
│  Node.js Version: [18.17.0 ▼]          │
│                                         │
│  Environment Variables:                 │
│  (vazio)                                │
│                                         │
│  [Save] [Cancel]                        │
│                                         │
│  Status: Stopped                        │
│  [Start] [Restart] [Stop]               │
│                                         │
│  [View Logs]                            │
│                                         │
└─────────────────────────────────────────┘
```

## 📝 Campos Explicados

### Startup File
- **O que é:** Nome do arquivo que inicia o servidor
- **O que colocar:** `server.js`
- **Importante:** Sem caminho, sem barras, só o nome do arquivo

### Node.js Version
- **O que é:** Versão do Node.js a usar
- **O que escolher:** Qualquer versão 18.x ou 20.x
- **Exemplos:** `18.17.0`, `20.9.0`, etc.

### Status
- **Stopped:** Servidor parado (precisa clicar em "Start")
- **Running:** Servidor rodando (está funcionando)

## 🎬 Sequência de Ações

### 1. Configurar
```
1. Clique em "Node.js" no menu
2. Clique em "Manage" no seu domínio
3. Preencha:
   - Startup File: server.js
   - Node.js Version: 18.x
4. Clique em "Save"
```

### 2. Iniciar
```
1. Verifique o Status
2. Se estiver "Stopped", clique em "Start"
3. Aguarde alguns segundos
4. Status deve mudar para "Running"
```

### 3. Verificar
```
1. Clique em "View Logs"
2. Procure por mensagens de sucesso
3. Teste: https://seudominio.com/api/health
```

## ⚠️ Se Você NÃO Vê "Node.js"

Se você **não vê** a opção "Node.js" no menu, significa:

- ❌ Você tem plano **GRATUITO**
- ❌ Plano gratuito **NÃO inclui Node.js**
- ✅ Você precisa de uma alternativa

### Alternativas:

1. **Render.com** (Recomendado)
   - Node.js gratuito
   - MySQL gratuito
   - Muito fácil

2. **Versão PHP**
   - Funciona no InfinityFree gratuito
   - Mesma funcionalidade
   - Posso criar para você

3. **Outros serviços**
   - Railway.app
   - Fly.io
   - Glitch.com

Veja o arquivo `ALTERNATIVAS.md` para mais detalhes.

## 🆘 Precisa de Ajuda?

Se ainda tiver dúvidas:

1. Tire um print da tela do painel
2. Me mostre o que você vê
3. Ou me diga se você vê "Node.js" no menu

---

**💡 Lembre-se:** Se você não tem "Node.js" no menu, você não pode usar Node.js no InfinityFree. Use Render.com ou peça a versão PHP!

