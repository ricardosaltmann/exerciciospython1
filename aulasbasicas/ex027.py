"""Exercício Python 027:
 Faça um programa que leia o nome completo de uma pessoa,
  mostrando em seguida o primeiro e o último nome separadamente."""
nome = str(input("Digite o seu nome completo: \n")).strip().upper()
div = nome.split()

print("Analizando o seu nome ...........")
print("O seu primeiro nome é {} e o seu ultimo nome é {}".format(div[0], div[-1]))