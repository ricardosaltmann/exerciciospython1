"""
Exercício Python 051:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
Mostre os 10 primeiros termos dessa progressão.
"""
print("="*40)
print('{:=^40}'.format('10 TERMOS DE UMA PA'))
print("="*40)

primeiro = int(input("Primeiro Termo: "))
razão = int(input("Razão:"))
contador = primeiro + (10 -1) * razão ### formula para encontrar o 10º termo
for c in range(primeiro, contador, razão):
    print(c, end=' → ')
print("ACABOU")