"""
Exercício Python 057:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
"""

sexo = str(input("Informe o sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados invalidos. Por favor informe o sexo:")).strip().upper()[0]
print("Sexo {} resgistrado com sucesso !".format(sexo))

