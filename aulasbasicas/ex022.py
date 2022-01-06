#########
"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome = str(input("Qual é o seu nome ? \n")).strip()
nome = nome.capitalize()
div = nome.split()
print(div)

print("O seu nome em maiusculas é: ", nome.upper())
print("O seu nome em minusculas é: ", nome.lower())
print("O seu nome completo tem {} letras".format(len(nome)-nome.count(" ")))
print("O seu primeiro nome tem ", nome.find(" "))
print("O seu primeiro nome é {} e ele tem {} letras".format(div[0], len(div[0])))

