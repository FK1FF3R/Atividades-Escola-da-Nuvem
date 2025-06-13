import random
import string
import requests

# EXERCÍCIO PRÁTICO 1
def gerar_senha():
    print("=== EXERCÍCIO 1: GERADOR DE SENHA ===")
    try:
        tamanho = int(input("Informe o número de caracteres da senha: "))
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print("Senha gerada:", senha)
    except ValueError:
        print("Valor inválido. Insira um número inteiro.")

# EXERCÍCIO PRÁTICO 2
def gerar_perfil_usuario():
    print("\n=== EXERCÍCIO 2: PERFIL ALEATÓRIO ===")
    try:
        response = requests.get('https://randomuser.me/api/')
        data = response.json()
        user = data['results'][0]
        nome = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    except Exception as e:
        print("Erro ao consultar a API:", e)

# EXERCÍCIO PRÁTICO 3
def consultar_cep():
    print("\n=== EXERCÍCIO 3: CONSULTA DE CEP ===")
    cep = input("Digite o CEP (somente números): ").strip()
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido.")
        return
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        dados = response.json()
        if 'erro' in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    except Exception as e:
        print("Erro na consulta do CEP:", e)

# EXERCÍCIO PRÁTICO 4
def consultar_cotacao():
    print("\n=== EXERCÍCIO 4: COTAÇÃO DE MOEDA ===")
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        response = requests.get(url)
        dados = response.json()
        key = f"{moeda}BRL"
        if key not in dados:
            print("Moeda não encontrada.")
            return
        info = dados[key]
        print(f"Moeda: {moeda}")
        print(f"Valor atual: R${info['bid']}")
        print(f"Máximo: R${info['high']}")
        print(f"Mínimo: R${info['low']}")
        print(f"Última atualização: {info['create_date']}")
    except Exception as e:
        print("Erro na consulta de cotação:", e)

# MENU DE EXECUÇÃO
def menu():
    while True:
        print("\n--- MENU DE EXERCÍCIOS ---")
        print("1. Gerar senha aleatória")
        print("2. Gerar perfil de usuário aleatório")
        print("3. Consultar endereço por CEP")
        print("4. Consultar cotação de moeda")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            gerar_senha()
        elif escolha == '2':
            gerar_perfil_usuario()
        elif escolha == '3':
            consultar_cep()
        elif escolha == '4':
            consultar_cotacao()
        elif escolha == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
