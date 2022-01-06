"""
Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
n = int(input("Digite um número para verificar se ele é primo:"))
mult = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')

if mult == 2:
    print("\n\033[mO número {} é um numero primo pois é divisivel apenas por ele mesmo e por 1".format(n))
else:
    print("\n\033[mO número {} foi divisivel por {} vezes e por ser divisivel por mais de 2X ele não é um número primo "
          .format(n, mult))
