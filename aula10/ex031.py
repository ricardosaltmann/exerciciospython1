"""Exercício Python 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas."""
from random import randint
distancia = randint(1, 1000)
print("Você esta prestes a iniciar uma viagem de {}Km".format(distancia))
if distancia > 200:
    valor = distancia * 0.45
    print("O valor da passagem é de R${:.2f}".format(valor))
else:
    valor = distancia * 0.50
    print("O valor da sua passagem é R${:.2f}".format(valor))