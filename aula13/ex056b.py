"""
Exercício Python 056:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

media = 0
maioridadehome = 0
nomevelho = ''
contamulher = 0
for pesquisa in range(1, 5):
    print("------ {}ª PESSOA ------ ".format(pesquisa))
    nome = str(input("Nome:")).strip()
    idade = (int(input("Idade:")))
    media += idade
    sexo = str(input("Sexo [M/F]")).strip()
    if pesquisa == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if idade > maioridadehome and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    else:
        if sexo in 'Ff' and idade < 20:
            contamulher += 1

print("A média de idade do grupo é {}".format(media / 4))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehome, nomevelho))
print("Ao todo temos {} mulheres mais novas que 20 anos".format(contamulher))
