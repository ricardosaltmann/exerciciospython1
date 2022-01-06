'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

dados = list()
lista = dict()
soma = media = 0
mulheres = []
while True:
    lista.clear()
    lista["Nome"] = str(input("Nome:")).capitalize()
    while True:
        lista["Sexo"] = str(input("Sexo: [F/M]")).strip().upper()
        if lista['Sexo'] in 'MF':
            break
        print("ERRO! Por favor digite apenas M ou F")
    lista["Idade"] = int(input("Idade:"))
    soma += lista["Idade"]
    dados.append(lista.copy())
    while True:
        prox = str(input("Quer continuar? [S/N]").strip().upper())
        if prox in 'NS':
            break
        print("ERRO! Responda apenas S ou N")
    if prox in 'N':
        break
print("-=" * 40)
print(f"A) Ao todo temos {len(dados)} pessoas cadastradas.")
media = soma / len(dados)
print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end='')
for p in dados:
    if p["Sexo"] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print(f"D) Lista das pessoas que estão acima da média: ")
for p in dados:
    if p["Idade"] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print("<< FINALIZANDO  >>")


