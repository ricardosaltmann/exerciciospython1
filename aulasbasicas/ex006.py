import math, cmath

print("Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.")
n = int(input("Digite um número \n"))
dobro = n * 2
triplo = n * 3
raiz = math.pow(n, 0.5)
raiz1 = (n ** (0.5))
print("O dobro de {} é {} e o triplo é {} e tem raiz quadrada de {}".format(n, dobro, triplo, raiz))
print(cmath.sqrt(n))
print(raiz1)
