"""
Exercício Python 090:
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.

"""

aluno = {}
while True:
    aluno['Nome'] = str(input("Nome: "))
    aluno['Média'] = float(input("Média: "))

    if aluno['Média'] > 7.0:
        aluno['Situacao'] = 'Aprovado'
    elif 5 <= aluno['Média'] < 7:
        aluno['Situacao'] = 'Recuperação'
    else:
        aluno['Situacao'] = 'Reprovado'
    for k, v in aluno.items():
        print(f"{k} = {v}")

    opc = str(input("Outro aluno? [S/N]")).strip().upper()
    if opc in 'Nn':
        break
    else:
        aluno.clear()