"""
Exercício Python 098:
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def contagem(i, f, r):
    if r < 0:
        r *= -1
    if r == 0:
        r = 1
    print('-=' * 30)
    print(f"Contagem de {i} até {f} de {r} em {r}")
    sleep(2)

    if i < f:
        while i <= f:
            print(f'{i} ', end='')
            i += r
            sleep(0.5)
        print("FIM!")
    elif i > f:
        while f <= i:
            print(f'{i} ', end='')
            i -= r
            sleep(0.5)
        print("FIM!")




contagem(1, 10, 1)
contagem(10, 0, 2)

print('-=' * 30)
print("Agora é a sua vez de personalizar a lista")
while True:
    i = int(input("Inicio: "))
    f = int(input("Fim: "))
    r = int(input("Passo: "))
    contagem(i, f, r)
    per = str(input("Quer continuar? [S/N]")).upper()[0]
    if per in 'Nn':
        print("Finalizando.....")
        break
