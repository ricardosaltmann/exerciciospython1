'''
Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

num = []
maior = 0
menor = 0
for cont in range(0, 5):
    num.append(int(input(f"Digite um valor pra a posição {cont}: ")))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print('=-' * 30)
print(f"Você digitou os valores {num}")
print(f'O Maior número digitado foi {maior} nas possições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O Menor número digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()

