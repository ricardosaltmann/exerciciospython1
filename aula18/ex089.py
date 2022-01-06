"""
Exercício Python 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
"""

sala = []
aluno = []
contador = 0
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    sala.append([nome, [nota1, nota2], media])
    proximo = str(input("Quer continuar? [S/N]")).strip().upper()
    if proximo in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'* 26)
for i, a in enumerate(sala):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print('-' * 30)
while True:
    mn = int(input("Mostrar notas de qual aluno? (999 para sair): "))
    if mn == 999:
        print("Finalizando...")
        break
    if mn <= len(sala) - 1:
        print(f"Notas de {sala[mn] [0]} são Nota 1: {sala[mn] [1] [0]} e Nota 2: {sala[mn] [1] [1]}")


