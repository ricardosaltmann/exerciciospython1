'''
Exercício Python 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
ano_atual = date.today()
cad = {}
cad["Nome"] = str(input("Nome: "))
cad["Nascimento"] = int(input("Ano de Nascimento: "))
cad["Idade"] = ano_atual.year - cad["Nascimento"]
cad["CTPS"]= int(input("Carteira de trabalho (O para não tem):"))
if cad["CTPS"] != 0:
    cad["Contratacao"] = int(input("Ano do 1º registro: "))
    cad["Aposentará"] = cad["Idade"] + (cad['Contratacao'] + 35) - ano_atual.year
    cad["Salario"] = float(input("Salario: R$"))
print("-=" * 40)
for k, v in cad.items():
    print(f"{k} tem o valor {v}")