from random import randint
from time import sleep
from random import randint


def analizando():
    print("Analisando os valores passados", end='')
    c = 0
    for c in range(0, 6):
        print('.', end='')
        sleep(0.3)
    print()

lista1 = list()
def maior(lista):
    n = randint(1, 25)
    for c in range(0, n):
        ns = randint(1, 100)
        lista.append(ns)
    contador = 0
    for v in lista:
        lista1.append((f"{v}, "))
        contador += 1
    print()
    lista = lista1
    analizando()
    maior = 0
    for v in lista:
        print(f"{v} ", end='')
        sleep(0.5)
        if maior == 0:
            maior = v
        elif v > maior:
            maior = v

    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f"O maior valor informado foi {maior}")
    print('-=' * 30)

for c in range(0, randint(1,8)):
    numeros = list()
    maior(numeros)
