print("Exercício Python 013:"
      "Faça um algoritmo que leia o salário de um funcionário"
      " e mostre seu novo salário, com 15% de aumento.")
salario = float(input("Digite o valor do seu salario"))
aumento = 0.15 * salario

print("O valor do salario após o aumento de 15% será de {}".format(salario + aumento))