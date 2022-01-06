"""
Exercício Python 054:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from random import randint
idade1 = randint(1951, 2021)
idade2 = randint(1951, 2021)
idade3 = randint(1951, 2021)
idade4 = randint(1951, 2021)
idade5 = randint(1951, 2021)
idade6 = randint(1951, 2021)
idade7 = randint(1951, 2021)
ano = 2021
maior = 0
menor = 0
print('Em que ano a 1ª pessoa nasceu? \033[34m{}\033[m'.format(idade1))
print('Em que ano a 2ª pessoa nasceu? \033[34m{}\033[m'.format(idade2))
print('Em que ano a 3ª pessoa nasceu? \033[34m{}\033[m'.format(idade3))
print('Em que ano a 4ª pessoa nasceu? \033[34m{}\033[m'.format(idade4))
print('Em que ano a 5ª pessoa nasceu? \033[34m{}\033[m'.format(idade5))
print('Em que ano a 6ª pessoa nasceu? \033[34m{}\033[m'.format(idade6))
print('Em que ano a 7ª pessoa nasceu? \033[34m{}\033[m'.format(idade7))
lista = [idade1, idade2, idade3, idade4, idade5, idade6, idade7]
lista.sort()
print(lista, end=' ')
print("")
for i in lista:
    if ano - i >= 18:
        maior += 1
    else:
        menor += 1
print("Ao todo foram contabilizados {} maiores de idade".format(maior))
print("E {} menores de idade".format(menor))
