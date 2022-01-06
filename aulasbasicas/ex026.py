"""Exercício Python 026:
 Faça um programa que leia uma frase pelo teclado
 e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez
 e em que posição ela aparece a última vez."""

nome = str(input("Digite o seu nome completo \n")).strip()
nome = nome.upper()
div = nome.split()
letrasp = len(div[0])
print(letrasp)

print("O seu nome tem {}".format(len(nome)))
print("O seu nome tem {} letras A".format(nome.count("A")))
print("Ela aparece na primeira vez na possição {}".format(nome.find("A")+1))
print("A letra 'A' aparece pela ultima vez na possição {}".format(nome.rfind("A")+1))
