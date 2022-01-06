'''
Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f"Digite o {c +1}º valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f"Os valores pares digitados foram {lista[0]}")
print(f"Os valores impares digitados foram {lista[1]}")

