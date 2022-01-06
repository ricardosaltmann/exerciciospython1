'''
Exercício Python 096:
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
'''

def terreno(l, c):
    area = (l * c)
    print(f'A area de um terreno de {l}m de largura por {c}m de comprimento é igual a {area}m')


print("Controle de Terrenos")
print('-' * 30)
l = float(input("Largura (m) "))
c = float(input("Comprimento (m) "))
terreno(l, c)

