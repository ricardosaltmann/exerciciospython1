"""Exercício Python 024:
 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

cidade = str(input("Digite o nome da sua Cidade: \n")).strip()
cidade = cidade.upper()
div = cidade.split()
if div[0] != "SANTO":
    print(" A sua cidade não começa com Santo")
else:
    print("O nome da sua cidade começa com SANTO")

##print da variavel e contando de 0 a 5 para pegar as 4 primeiras letras, depois comparando com santo.
print(cidade[:5] == 'SANTO')
