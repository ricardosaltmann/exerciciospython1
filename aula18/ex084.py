'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
pessoas = []
dado = []
obeso = []
magro = []

while True:
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite o peso: ")))
    pessoas.append(dado[:])
    dado.clear()
    c = str(input("Quer continuar? [S/N] "))
    if c in 'Nn':
        break
for i, v in enumerate(pessoas):
    if v[1] >= 90:
        obeso += v
    else:
        magro += v

print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"As pessoas mais pesadas são {obeso}")
print(f"As pessoas mais leves são {magro}")
