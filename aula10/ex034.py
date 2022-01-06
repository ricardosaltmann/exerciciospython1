"""Exercício Python 034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais,o aumento é de 15%."""

salario = float(input("Qual é o seu salario? "))

if salario <= 1250:
    salarioa = salario * 1.15              # metodo 1 de %
    novo = salario + (salario * 15 / 100)  # metodo 2 de %
else:
    salarioa = salario * 1.10
    novo = salario + (salario * 10 / 100)
print("O seu salario passou de R${:.2f} para R${:.2f} ".format(salario, salarioa))
print("O seu salario passou de R${:.2f} para R${:.2f} ".format(salario, novo))




