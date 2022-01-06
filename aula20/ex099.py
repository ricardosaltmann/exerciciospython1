"""
Exercício Python 099:
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep
from random import randint


def analizando():
    print("Analisando os valores passados", end='')
    c = 0
    for c in range(0, 6):
        print('.', end='')
        sleep(0.3)
    print()


def maior(* num):
    analizando()
    maior = 0
    for v in num:
        print(f"{v} ", end='')
        sleep(0.5)
        if maior == 0:
            maior = v
        elif v > maior:
            maior = v

    print(f'Foram informados {len(num)} valores ao todo.')
    print(f"O maior valor informado foi {maior}")
    print('-=' * 30)



maior(95, 88, 77, 47, 51, 99, 69, 78, 71, 20, 78, 47, 9, 44, 68, 11, 94, 3, 83, 73, 34, 82, 4, 15, 20, 20)
maior(52, 25, 23, 67, 76, 61, 97, 79, 57, 92, 68, 60, 60)
maior(57, 39, 10, 49, 85, 30, 1, 66, 95, 27, 27)
maior(48, 8, 89, 55, 45, 45)
maior(74, 49, 95, 34, 25, 25)
