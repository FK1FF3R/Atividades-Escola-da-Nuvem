import csv
import json
import pandas as pd
import statistics

# ATIVIDADE 01
def atividade_01():
    print("ATIVIDADE 01:")
    df = pd.read_csv('log_treinamento.csv')  # Nome do arquivo com log
    if 'tempo_execucao' in df.columns:
        tempos = df['tempo_execucao']
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos)
        print(f"Média: {media:.2f}")
        print(f"Desvio padrão: {desvio:.2f}")
    else:
        print("Coluna 'tempo_execucao' não encontrada no arquivo.")

# ATIVIDADE 02
def atividade_02():
    print("\nATIVIDADE 02:")
    pessoas = [
        {'Nome': 'Alice', 'Idade': 30, 'Cidade': 'São Paulo'},
        {'Nome': 'Bruno', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
        {'Nome': 'Carla', 'Idade': 28, 'Cidade': 'Belo Horizonte'}
    ]
    with open('pessoas.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=['Nome', 'Idade', 'Cidade'])
        writer.writeheader()
        writer.writerows(pessoas)
    print("Arquivo 'pessoas.csv' criado com sucesso.")

# ATIVIDADE 03
def atividade_03():
    print("\nATIVIDADE 03:")
    try:
        with open('pessoas.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                print(linha)
    except FileNotFoundError:
        print("Arquivo 'pessoas.csv' não encontrado. Execute a Atividade 02 primeiro.")

# ATIVIDADE 04
def atividade_04():
    print("\nATIVIDADE 04:")
    pessoa = {
        "nome": "Daniela",
        "idade": 35,
        "cidade": "Curitiba"
    }

    with open("pessoa.json", "w", encoding='utf-8') as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)
    print("Dados escritos em 'pessoa.json'.")

    with open("pessoa.json", "r", encoding='utf-8') as f:
        dados_lidos = json.load(f)
        print("Dados lidos do JSON:", dados_lidos)

atividade_01()
atividade_02()
atividade_03()
atividade_04()
