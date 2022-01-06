"""Exercício Python 035:
 Desenvolva um programa que leia o comprimento de três retas
  e diga ao usuário se elas podem ou não formar um triângulo."""

s1 = float(input("Digite o Primeiro seguimento: "))
s2 = float(input("Digite o Segundo seguimento: "))
s3 = float(input("Digite o Terceiro seguimento: "))

lista = [s1, s2, s3]
lista.sort()
print(lista)
if lista[0] + lista[1] <= lista[2]:
    print("A soma dos seguimentos acima pode formar um triangulo")
else:
    print("A soma dos seguimentos acima não pode formar um triangulo")

#### metodo Guanabara
if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print("A soma dos seguimentos acima pode formar um triangulo")
else:
    print("A soma dos seguimentos acima não pode formar um triangulo")