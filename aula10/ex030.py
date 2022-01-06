"Exercício Python 030: "
"Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."
from random import randint
numero = randint(0, 9999)

if numero % 2 == 0:
    print("O {} é um número Par".format(numero))
else:
    print("O número {} é Impar".format(numero))
