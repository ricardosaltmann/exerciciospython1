"""Exercício Python 023: Faça um programa que leia um número de 0 a 9999
 e mostre na tela cada um dos dígitos separados.
"""

numero = int(input("Digite um numero inteiro de 0 a 9999 \n"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analizando o número {}".format(numero))
print("O seu número tem: {} unidade".format(u))
print("O seu número tem {} Dezenas".format(d))
print("O seu número tem {} Centenas".format(c))
print("O seu número tem {} Milhares".format(m))

