"""
Exercício Python 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""
l1 = float(input("Primeiro seguimento: "))
l2 = float(input("Segundo seguimento: "))
l3 = float(input("Terceiro seguimento: "))

if l1 + l2 <= l3 or l2 + l3 <= l1 or l3 + l1 <= l2:
    print("Com essas medidas não é possivel formar um triangulo")
elif l1 == l2 and l3 == l1:
    print("As medidas acima PODEM FORMAR um triangulo e ele é um triangulo EQUILÁTERO")
elif l1 != l2 and l2 != l3 and l3 != l1:
    print("As medidas acima PODEM FORMAR um triangulo e ele é um triangulo ESCALENO")
else:
    print("As medidas acima PODEM FORMAR um triangulo e ele é um triangulo ISÓSCELES")
