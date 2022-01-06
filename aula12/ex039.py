"""
Exercício Python 039:
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime
date = datetime.date.today()
ano = date.year

dnascimento = int(input("Informe o ano de nascimento:"))
idade = ano - dnascimento

if idade < 18:
    dif = (18 - idade) + ano
    print("Você tem {} anos, e ainda vai se alistar no serviço militar no ano de {}".format(idade, dif))
elif idade > 18:
    dif = ano - (idade - 18)
    print("Quem nasceu em {} tem {} em {}".format(dnascimento, idade, ano))
    print("Já se passaram {} para o alistamento".format(ano - dif))
    print("Seu alistamento foi em {}".format(dif))
else:
    print("Quem nasceu em {}, tem {} anos em {}".format(dnascimento, idade, ano))
    print("Você deve se alistar IMEDIATAMENTE!")