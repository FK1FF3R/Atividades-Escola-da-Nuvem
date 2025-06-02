## 1- Calculadora de Gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")

## 2- Verificar Palíndromo

def eh_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")

## 3- Verificar Senha Forte

def senha_forte(senha):
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        return True
    return False

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando...")
        break
    elif senha_forte(senha):
        print("Senha forte cadastrada com sucesso!")
        break
    else:
        print("Senha fraca. Tente novamente.")
