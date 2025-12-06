# 🔑 KeyAuth Generator

Sistema completo de geração e gerenciamento de keys de autenticação para seus programas.

## 📋 Funcionalidades

- ✅ Geração de keys únicas e seguras
- ✅ Validação de keys em tempo real
- ✅ Controle de expiração (dias de validade)
- ✅ Gerenciamento completo (ativar/desativar/deletar)
- ✅ Estatísticas e relatórios
- ✅ Interface web moderna e responsiva
- ✅ API REST para integração com seus programas

## 🚀 Instalação

### Pré-requisitos

- Node.js (versão 14 ou superior)
- npm (geralmente vem com Node.js)
- Banco de dados MySQL (configurado no arquivo `config/database.js`)

### Configuração do Banco de Dados

O sistema está configurado para usar MySQL (InfinityFree). As configurações estão em `config/database.js`:

```javascript
host: 'sql305.infinityfree.com',
user: 'if0_40460911',
password: 'zlshop12345',
database: 'if0_40460911_keyauth'
```

**A tabela será criada automaticamente na primeira execução!**

### Passos

1. **Instalar dependências:**
```bash
npm install
```

2. **Iniciar o servidor:**
```bash
npm start
```

O servidor irá:
- Testar a conexão com MySQL
- Criar a tabela automaticamente se não existir
- Iniciar na porta 3000

3. **Acessar a interface:**
Abra seu navegador em: `http://localhost:3000`

### Testar o Sistema

Para testar se tudo está funcionando, execute o script Python de teste:

```bash
# Instalar dependências Python
pip install -r requirements.txt

# Executar testes
python test_keyauth.py
```

## 📖 Como Usar

### Interface Web

1. **Gerar uma Key:**
   - Preencha o nome do programa
   - (Opcional) Defina dias de validade
   - (Opcional) Adicione observações
   - Clique em "Gerar Key"

2. **Validar uma Key:**
   - Digite a key e o nome do programa
   - Clique em "Validar Key"

3. **Gerenciar Keys:**
   - Visualize todas as keys na lista
   - Use a busca para filtrar
   - Ative/desative ou delete keys conforme necessário

### Integração com Seus Programas

#### Exemplo em Python:

```python
import requests
import json

def validar_key(key, programa):
    url = "http://localhost:3000/api/validate"
    dados = {
        "key": key,
        "program": programa
    }
    
    try:
        resposta = requests.post(url, json=dados)
        resultado = resposta.json()
        
        if resultado.get("valid"):
            print("✅ Key válida!")
            if resultado.get("daysRemaining"):
                print(f"Dias restantes: {resultado['daysRemaining']}")
            return True
        else:
            print(f"❌ {resultado.get('message', 'Key inválida')}")
            return False
    except Exception as e:
        print(f"Erro ao validar: {e}")
        return False

# Uso
if validar_key("SUA-KEY-AQUI", "MeuPrograma.exe"):
    print("Programa autorizado!")
    # Seu código aqui
else:
    print("Acesso negado!")
    exit()
```

#### Exemplo em C#:

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class KeyAuth
{
    private static readonly HttpClient client = new HttpClient();
    private const string API_URL = "http://localhost:3000/api/validate";

    public static async Task<bool> ValidarKey(string key, string programa)
    {
        try
        {
            var dados = new
            {
                key = key,
                program = programa
            };

            var json = JsonSerializer.Serialize(dados);
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await client.PostAsync(API_URL, content);
            var responseContent = await response.Content.ReadAsStringAsync();
            var resultado = JsonSerializer.Deserialize<JsonElement>(responseContent);

            if (resultado.GetProperty("valid").GetBoolean())
            {
                Console.WriteLine("✅ Key válida!");
                if (resultado.TryGetProperty("daysRemaining", out var days))
                {
                    Console.WriteLine($"Dias restantes: {days.GetInt32()}");
                }
                return true;
            }
            else
            {
                Console.WriteLine($"❌ {resultado.GetProperty("message").GetString()}");
                return false;
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Erro ao validar: {e.Message}");
            return false;
        }
    }
}

// Uso
static async Task Main()
{
    if (await KeyAuth.ValidarKey("SUA-KEY-AQUI", "MeuPrograma.exe"))
    {
        Console.WriteLine("Programa autorizado!");
        // Seu código aqui
    }
    else
    {
        Console.WriteLine("Acesso negado!");
        Environment.Exit(0);
    }
}
```

#### Exemplo em JavaScript/Node.js:

```javascript
const axios = require('axios');

async function validarKey(key, programa) {
    try {
        const response = await axios.post('http://localhost:3000/api/validate', {
            key: key,
            program: programa
        });
        
        if (response.data.valid) {
            console.log('✅ Key válida!');
            if (response.data.daysRemaining) {
                console.log(`Dias restantes: ${response.data.daysRemaining}`);
            }
            return true;
        } else {
            console.log(`❌ ${response.data.message}`);
            return false;
        }
    } catch (error) {
        console.error('Erro ao validar:', error.message);
        return false;
    }
}

// Uso
(async () => {
    if (await validarKey('SUA-KEY-AQUI', 'MeuPrograma.exe')) {
        console.log('Programa autorizado!');
        // Seu código aqui
    } else {
        console.log('Acesso negado!');
        process.exit(0);
    }
})();
```

## 🔌 API Endpoints

### POST `/api/generate`
Gera uma nova key.

**Body:**
```json
{
  "program": "NomeDoPrograma",
  "days": 30,
  "notes": "Observações opcionais"
}
```

**Resposta:**
```json
{
  "success": true,
  "key": {
    "id": "uuid",
    "key": "XXXX-XXXX-XXXX-XXXX",
    "program": "NomeDoPrograma",
    "createdAt": "2024-01-01T00:00:00.000Z",
    "expiresAt": "2024-01-31T00:00:00.000Z",
    "days": 30,
    "notes": "Observações opcionais",
    "isActive": true
  }
}
```

### POST `/api/validate`
Valida uma key.

**Body:**
```json
{
  "key": "XXXX-XXXX-XXXX-XXXX",
  "program": "NomeDoPrograma"
}
```

**Resposta:**
```json
{
  "valid": true,
  "message": "Key válida",
  "expiresAt": "2024-01-31T00:00:00.000Z",
  "daysRemaining": 15
}
```

### GET `/api/keys`
Lista todas as keys.

### GET `/api/keys/:id`
Obtém uma key específica.

### PUT `/api/keys/:id`
Atualiza uma key (ativar/desativar).

**Body:**
```json
{
  "isActive": false,
  "notes": "Nova observação"
}
```

### DELETE `/api/keys/:id`
Deleta uma key.

### GET `/api/stats`
Retorna estatísticas do sistema.

## 📁 Estrutura do Projeto

```
keyauth-generator/
├── server.js          # Servidor Node.js/Express
├── package.json       # Dependências do projeto
├── README.md          # Este arquivo
├── database/          # Banco de dados (JSON)
│   └── keys.json      # Keys armazenadas
└── public/            # Frontend
    ├── index.html     # Interface principal
    ├── styles.css     # Estilos
    └── script.js      # JavaScript do frontend
```

## 🔒 Segurança

- As keys são geradas usando criptografia segura
- Validação de entrada em todas as rotas
- Controle de expiração automático
- Sistema de ativação/desativação

## 📝 Notas

- O banco de dados está configurado para MySQL (InfinityFree)
- A tabela `keys` é criada automaticamente na primeira execução
- Configure HTTPS para uso em produção
- Adicione autenticação de administrador se necessário
- Para alterar as configurações do banco, edite `config/database.js`

## 🛠️ Desenvolvimento

Para desenvolvimento com auto-reload:

```bash
npm run dev
```

## 📄 Licença

MIT

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias!

