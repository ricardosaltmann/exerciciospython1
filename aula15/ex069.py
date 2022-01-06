"""
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
mulheres20 = 0
mais18 = 0
homem = 0
while True:
    print("-" * 40)
    print('{:=^40}'.format('CADASTRE UMA PESSOA'))
    print("-" * 40)

    i = int(input("Idade: "))
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo in 'MF':
            sexo = sexo
            break
        else:
            print("sexo precisa ser [M/F]")
    new = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if i > 18:
        mais18 += 1
    if sexo == 'F' and i < 20:
        mulheres20 += 1
    if new == 'N':
        break
print('=-='* 40)
print(f"O total de pessoas com mais de 18 anos são: {mais18}")
print('_'* 40)
print(f"Foram cadasdastrados  {homem} Homens")
print('_'* 40)
print(f"E temos {mulheres20} mulheres com menos de 20 anos")
print('=-='* 40)