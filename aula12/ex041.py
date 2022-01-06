"""
Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
from datetime import date

dnascimento = int(input("Qual é o ano de nascimento?"))
ano = date.today().year
idade = ano - dnascimento

if idade <= 9:
    print("Quem nasceu no ano de {} tem {} anos".format(ano, idade))
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Quem nasceu no ano de {} tem {} anos".format(ano, idade))
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Quem nasceu no ano de {} tem {} anos".format(ano, idade))
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Quem nasceu no ano de {} tem {} anos".format(ano, idade))
    print("Classificação: SENIOR")
else:
    print("Quem nasceu no ano de {} tem {} anos".format(ano, idade))
    print("Classificação: MASTER")

