'''
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso:
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
par = []
impar = []
while True:
    v = int(input("Digite um número: "))
    lista.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
    c = str(input("Quer continuar? [S/N]"))
    while c not in 'SsNn':
        c = str(input("Quer continuar? [S/N]"))
    if c in 'Nn':
        break
print('-=' * 30)
print(f"A lista compreta é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de impares é {impar}")


