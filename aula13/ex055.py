"""
Exercício Python 055:
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
lista = []
for peso in range(1, 6):
    p = float(input("Peso da {}ª pessoa: ".format(peso)))
    lista.append(p)
print("resultado lista ", lista)
lista.sort()
print("O maior peso digitado foi {}kg".format(lista[4]))
print("O menor peso digitado foi {}kg".format(lista[0]))