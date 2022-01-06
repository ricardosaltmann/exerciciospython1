"""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
print("_" * 40)
print('{: ^40}'.format('LOJA SUPER BARATÃO'))
print("_" * 40)
totalc = 0
maisb = 0
precomb = 0
maisdmil = 0
contador = 0
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    totalc += preco
    contador += 1
    if contador == 1:
        maisb = produto
        precomb = preco
    if preco < precomb:
        maisb = produto
        precomb = preco
    if preco > 1000:
        maisdmil += 1

    cont = ' '
    while cont not in 'NnSs':
        cont = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if cont == 'N':
        break

print("{:-^40}".format('FIM DO PROGRAMA'))
print(f"O total da compra foi {totalc}")
print(f"Temos {maisdmil} produtos custando mais que R$1000.00")
print(f"O produto mais barato foi {maisb} que custa R${precomb}")