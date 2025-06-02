## 1- Classificador de Idade

def classificador_de_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Por favor, digite uma idade válida (número positivo).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if 0 <= idade <= 12:
        classificacao = "Criança"
    elif 13 <= idade <= 17:
        classificacao = "Adolescente"
    elif 18 <= idade <= 59:
        classificacao = "Adulto"
    else:
        classificacao = "Idoso"

    print(f"Com {idade} anos, você é classificado como: {classificacao}")

classificador_de_idade()

## 2- Calculadora de IMC

def calculadora_de_imc():
    while True:
        try:
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            if peso <= 0:
                print("Por favor, digite um peso válido.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    while True:
        try:
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))
            if altura <= 0:
                print("Por favor, digite uma altura válida.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

calculadora_de_imc()

## 3- Conversor de Temperatura

def conversor_de_temperatura():
    while True:
        try:
            temp_origem = float(input("Digite a temperatura a ser convertida: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a temperatura.")

    print("\nUnidades de Temperatura:")
    print("C - Celsius")
    print("F - Fahrenheit")
    print("K - Kelvin")

    while True:
        unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
        if unidade_origem in ['C', 'F', 'K']:
            break
        else:
            print("Unidade de origem inválida. Tente novamente.")

    while True:
        unidade_destino = input("Digite a unidade para qual deseja converter (C, F, K): ").upper()
        if unidade_destino in ['C', 'F', 'K']:
            break
        else:
            print("Unidade de destino inválida. Tente novamente.")

    resultado = 0
    convertido_de_para = f"{unidade_origem} para {unidade_destino}"

    if unidade_origem == unidade_destino:
        resultado = temp_origem
        print(f"\nA temperatura é a mesma: {resultado:.2f}°{unidade_destino}")
        return

    if unidade_origem == 'C':
        if unidade_destino == 'F':
            resultado = (temp_origem * 9/5) + 32
        elif unidade_destino == 'K':
            resultado = temp_origem + 273.15

    elif unidade_origem == 'F':
        if unidade_destino == 'C':
            resultado = (temp_origem - 32) * 5/9
        elif unidade_destino == 'K':
            resultado = (temp_origem - 32) * 5/9 + 273.15

    elif unidade_origem == 'K':
        if unidade_destino == 'C':
            resultado = temp_origem - 273.15
        elif unidade_destino == 'F':
            resultado = (temp_origem - 273.15) * 9/5 + 32

    print(f"\n{temp_origem:.2f}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")

conversor_de_temperatura()

## 4- Verificador de Ano Bissexto

def verificador_ano_bissexto():
    while True:
        try:
            ano = int(input("Digite um ano para verificar se é bissexto: "))
            if ano <= 0: # Anos geralmente são contados a partir de 1 d.C.
                print("Por favor, digite um ano válido (número positivo).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto. 🎉")
    else:
        print(f"O ano {ano} não é bissexto.")

verificador_ano_bissexto()