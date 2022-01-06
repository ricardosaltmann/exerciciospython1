"""
Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random
from random import sample
numale = (random.sample(range(100),5))
for n in numale:
    print(f"{n},", end=' ')


print(f"\nO maior número foi {max(numale)}")
print(f"O maior número foi {min(numale)}")



