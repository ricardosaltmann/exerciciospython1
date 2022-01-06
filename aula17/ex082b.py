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
    lista.append(int(input("Digite um número: ")))
    c = str(input("Quer continuar? [S/N]"))
    if c in 'Nn':
        break
print(f"A lista digitada é {lista}")
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f"A lista digitada contêm os números pares {par}")
print(f"A lista digitada contem os números impares {impar}")


