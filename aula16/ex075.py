"""
Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
num = (int(input(f"Digite um número:")),
       int(input("Digite outro número:")),
       int(input("Digite mais um número:")),
       int(input("Digite o ultimo número:")))




print(f"O numero 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O número 3 foi digitado na posição {num.index(3) + 1}")
else:
    print("Não foi digitado número 3")

print(f"Os números pares digitados foram: ", end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')





