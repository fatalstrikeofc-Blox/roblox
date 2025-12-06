"""
Script de teste completo para KeyAuth
Testa todas as funcionalidades do sistema
"""
import requests
import json
import time
from datetime import datetime

# Configuração
# IMPORTANTE: Altere para a URL do seu site no InfinityFree
# Exemplo: API_URL = "https://seudominio.com"
API_URL = "http://localhost:3000"  # Para teste local
# API_URL = "https://seudominio.infinityfreeapp.com"  # Descomente e use sua URL do InfinityFree

PROGRAMA_TESTE = "TestePrograma.exe"

def print_header(texto):
    """Imprime um cabeçalho formatado"""
    print("\n" + "="*60)
    print(f"  {texto}")
    print("="*60)

def print_success(mensagem):
    """Imprime mensagem de sucesso"""
    print(f"✅ {mensagem}")

def print_error(mensagem):
    """Imprime mensagem de erro"""
    print(f"❌ {mensagem}")

def print_info(mensagem):
    """Imprime mensagem informativa"""
    print(f"ℹ️  {mensagem}")

def testar_conexao():
    """Testa se o servidor está respondendo"""
    print_header("TESTE 1: Conexão com o Servidor")
    try:
        response = requests.get(f"{API_URL}/api/stats", timeout=5)
        if response.status_code == 200:
            print_success("Servidor está respondendo!")
            stats = response.json().get('stats', {})
            print_info(f"Total de keys no banco: {stats.get('total', 0)}")
            print_info(f"Keys ativas: {stats.get('active', 0)}")
            return True
        else:
            print_error(f"Servidor retornou código {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_error("Não foi possível conectar ao servidor!")
        print_info("Certifique-se de que o servidor está rodando (npm start)")
        return False
    except Exception as e:
        print_error(f"Erro inesperado: {e}")
        return False

def gerar_key(dias=None, notas=None):
    """Gera uma nova key"""
    print_header("TESTE 2: Gerar Nova Key")
    try:
        dados = {
            "program": PROGRAMA_TESTE,
            "days": dias,
            "notes": notas or "Key gerada pelo script de teste"
        }
        
        response = requests.post(
            f"{API_URL}/api/generate",
            json=dados,
            timeout=5
        )
        
        if response.status_code == 200:
            resultado = response.json()
            if resultado.get('success'):
                key_data = resultado.get('key', {})
                key_value = key_data.get('key')
                print_success(f"Key gerada com sucesso!")
                print_info(f"Key: {key_value}")
                print_info(f"Programa: {key_data.get('program')}")
                print_info(f"ID: {key_data.get('id')}")
                if key_data.get('expiresAt'):
                    print_info(f"Expira em: {key_data.get('expiresAt')}")
                else:
                    print_info("Sem data de expiração")
                return key_value
            else:
                print_error("Falha ao gerar key")
                return None
        else:
            print_error(f"Erro HTTP {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print_error(f"Erro ao gerar key: {e}")
        return None

def validar_key(key, programa, deve_ser_valida=True):
    """Valida uma key"""
    print_header(f"TESTE 3: Validar Key ({'deve ser válida' if deve_ser_valida else 'deve ser inválida'})")
    try:
        dados = {
            "key": key,
            "program": programa
        }
        
        response = requests.post(
            f"{API_URL}/api/validate",
            json=dados,
            timeout=5
        )
        
        if response.status_code == 200:
            resultado = response.json()
            valid = resultado.get('valid', False)
            
            if valid == deve_ser_valida:
                if valid:
                    print_success("Key válida (como esperado)!")
                    if resultado.get('daysRemaining') is not None:
                        print_info(f"Dias restantes: {resultado.get('daysRemaining')}")
                    if resultado.get('expiresAt'):
                        print_info(f"Expira em: {resultado.get('expiresAt')}")
                else:
                    print_success(f"Key inválida (como esperado): {resultado.get('message')}")
                return True
            else:
                print_error(f"Resultado inesperado! Key válida: {valid}")
                print_error(f"Mensagem: {resultado.get('message')}")
                return False
        else:
            print_error(f"Erro HTTP {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print_error(f"Erro ao validar key: {e}")
        return False

def listar_keys():
    """Lista todas as keys"""
    print_header("TESTE 4: Listar Todas as Keys")
    try:
        response = requests.get(f"{API_URL}/api/keys", timeout=5)
        
        if response.status_code == 200:
            resultado = response.json()
            keys = resultado.get('keys', [])
            print_success(f"Total de keys encontradas: {len(keys)}")
            
            if keys:
                print("\n📋 Keys encontradas:")
                for i, key in enumerate(keys[:5], 1):  # Mostrar apenas as 5 primeiras
                    status = "✅ Ativa" if key.get('isActive') else "❌ Inativa"
                    expirada = ""
                    if key.get('expiresAt'):
                        if datetime.fromisoformat(key.get('expiresAt').replace('Z', '+00:00')) < datetime.now():
                            expirada = " ⏰ EXPIRADA"
                    print(f"  {i}. {key.get('key')} - {key.get('program')} - {status}{expirada}")
                
                if len(keys) > 5:
                    print(f"  ... e mais {len(keys) - 5} keys")
            else:
                print_info("Nenhuma key encontrada no banco")
            
            return True
        else:
            print_error(f"Erro HTTP {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print_error(f"Erro ao listar keys: {e}")
        return False

def obter_estatisticas():
    """Obtém estatísticas do sistema"""
    print_header("TESTE 5: Estatísticas do Sistema")
    try:
        response = requests.get(f"{API_URL}/api/stats", timeout=5)
        
        if response.status_code == 200:
            resultado = response.json()
            stats = resultado.get('stats', {})
            
            print_success("Estatísticas obtidas com sucesso!")
            print(f"\n📊 Estatísticas:")
            print(f"  • Total de keys: {stats.get('total', 0)}")
            print(f"  • Keys ativas: {stats.get('active', 0)}")
            print(f"  • Keys inativas: {stats.get('inactive', 0)}")
            print(f"  • Keys expiradas: {stats.get('expired', 0)}")
            print(f"  • Programas diferentes: {stats.get('programs', 0)}")
            
            return True
        else:
            print_error(f"Erro HTTP {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print_error(f"Erro ao obter estatísticas: {e}")
        return False

def testar_key_invalida():
    """Testa validação de key inválida"""
    print_header("TESTE 6: Validar Key Inválida")
    key_invalida = "XXXX-XXXX-XXXX-XXXX"
    return validar_key(key_invalida, PROGRAMA_TESTE, deve_ser_valida=False)

def testar_key_programa_errado():
    """Testa validação com programa errado"""
    print_header("TESTE 7: Validar Key com Programa Errado")
    # Primeiro gera uma key
    key = gerar_key()
    if key:
        # Tenta validar com programa diferente
        return validar_key(key, "ProgramaErrado.exe", deve_ser_valida=False)
    return False

def main():
    """Função principal que executa todos os testes"""
    print("\n" + "🔑"*30)
    print("  SCRIPT DE TESTE KEYAUTH - SISTEMA COMPLETO")
    print("🔑"*30)
    print(f"\n⏰ Iniciado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"🌐 URL da API: {API_URL}")
    print(f"📦 Programa de teste: {PROGRAMA_TESTE}")
    
    resultados = []
    
    # Executar testes
    resultados.append(("Conexão", testar_conexao()))
    
    if resultados[0][1]:  # Se a conexão funcionou
        resultados.append(("Gerar Key", gerar_key(dias=30) is not None))
        resultados.append(("Listar Keys", listar_keys()))
        resultados.append(("Estatísticas", obter_estatisticas()))
        
        # Gerar uma key para testes de validação
        key_teste = gerar_key(dias=7, notas="Key para teste de validação")
        if key_teste:
            resultados.append(("Validar Key Válida", validar_key(key_teste, PROGRAMA_TESTE, deve_ser_valida=True)))
            resultados.append(("Validar Key Inválida", testar_key_invalida()))
            resultados.append(("Validar Programa Errado", testar_key_programa_errado()))
    
    # Resumo final
    print_header("RESUMO DOS TESTES")
    total = len(resultados)
    sucesso = sum(1 for _, resultado in resultados if resultado)
    falhas = total - sucesso
    
    for nome, resultado in resultados:
        status = "✅ PASSOU" if resultado else "❌ FALHOU"
        print(f"  {nome:.<40} {status}")
    
    print(f"\n📊 Resultado Final:")
    print(f"  • Total de testes: {total}")
    print(f"  • Sucessos: {sucesso} ✅")
    print(f"  • Falhas: {falhas} ❌")
    print(f"  • Taxa de sucesso: {(sucesso/total*100):.1f}%")
    
    if falhas == 0:
        print("\n🎉 Todos os testes passaram! Sistema funcionando perfeitamente!")
    else:
        print(f"\n⚠️  {falhas} teste(s) falharam. Verifique os erros acima.")
    
    print(f"\n⏰ Finalizado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\n" + "="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Teste interrompido pelo usuário.")
    except Exception as e:
        print(f"\n\n❌ Erro fatal: {e}")
        import traceback
        traceback.print_exc()

