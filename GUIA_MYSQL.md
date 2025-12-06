# 🗄️ Guia MySQL - KeyAuth Generator

## ✅ Configuração do Banco de Dados

O sistema já está configurado com suas credenciais do InfinityFree:

- **Host:** sql305.infinityfree.com
- **Database:** if0_40460911_keyauth
- **User:** if0_40460911
- **Password:** zlshop12345

## 🚀 Início Rápido

### 1. Instalar Dependências

```bash
npm install
```

### 2. Iniciar o Servidor

```bash
npm start
```

O servidor irá:
- ✅ Conectar automaticamente ao MySQL
- ✅ Criar a tabela `keys` se não existir
- ✅ Iniciar na porta 3000

### 3. Testar o Sistema

Execute o script Python de teste:

```bash
# Instalar dependências Python
pip install requests

# Ou usando o requirements.txt
pip install -r requirements.txt

# Executar testes
python test_keyauth.py
```

## 📊 Estrutura da Tabela

A tabela `keys` será criada automaticamente com a seguinte estrutura:

```sql
CREATE TABLE keys (
  id VARCHAR(36) PRIMARY KEY,
  key_value VARCHAR(50) UNIQUE NOT NULL,
  program VARCHAR(255) NOT NULL,
  created_at DATETIME NOT NULL,
  expires_at DATETIME NULL,
  days INT NULL,
  notes TEXT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  used_at DATETIME NULL,
  last_validated DATETIME NULL,
  validation_count INT DEFAULT 0
);
```

## 🔧 Alterar Configurações

Se precisar alterar as configurações do banco, edite o arquivo:

```
config/database.js
```

## 🧪 Script de Teste Python

O arquivo `test_keyauth.py` testa:

1. ✅ Conexão com o servidor
2. ✅ Geração de keys
3. ✅ Validação de keys válidas
4. ✅ Validação de keys inválidas
5. ✅ Listagem de keys
6. ✅ Estatísticas
7. ✅ Validação com programa errado

Execute para verificar se tudo está funcionando:

```bash
python test_keyauth.py
```

## 📝 Exemplo de Uso em Python

```python
import requests

def validar_key(key, programa):
    response = requests.post(
        'http://localhost:3000/api/validate',
        json={'key': key, 'program': programa}
    )
    return response.json().get('valid', False)

# Uso
if validar_key('SUA-KEY-AQUI', 'MeuPrograma.exe'):
    print('✅ Acesso autorizado!')
    # Seu código aqui
else:
    print('❌ Acesso negado!')
    exit()
```

## ⚠️ Importante

- Certifique-se de que o servidor Node.js está rodando antes de executar os testes
- O banco de dados MySQL deve estar acessível
- A tabela é criada automaticamente na primeira execução
- Todas as keys são armazenadas no MySQL, não mais em JSON

## 🆘 Solução de Problemas

### Erro de Conexão MySQL

Se aparecer erro de conexão:
1. Verifique se as credenciais estão corretas em `config/database.js`
2. Verifique se o banco de dados existe no InfinityFree
3. Verifique se o servidor MySQL está acessível

### Tabela não criada

A tabela é criada automaticamente. Se houver problemas:
1. Verifique as permissões do usuário MySQL
2. Verifique se o banco de dados existe
3. Veja os logs do servidor para mais detalhes

