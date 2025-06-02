## 1- Calculadora com Tratamento de Erros
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use +, -, * ou /.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as ve:
        print(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")

## 2- Registro de Notas da Turma

notas = []

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")


## 3 - Verificação de Senha Forte

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

## 4 - Par ou Ímpar com Contagem

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
