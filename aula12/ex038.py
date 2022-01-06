"""
Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
pn = int(input("Digite o primeiro número:"))
sn = int(input("Digite o segundo número:"))

if pn > sn:
    print("O primeiro valor é maior")
elif sn > pn:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")
