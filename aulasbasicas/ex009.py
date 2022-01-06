print("Exercício Python 009: Faça um programa que leia um número Inteiro qualquer"
      " e mostre na tela a sua tabuada.")

n = int(input("Digite um numero de 1 a 10"))
qtd = 0
print("_" * 12)
while qtd < 10:
      qtd = qtd + 1
      print("{} x {} = {}".format(n, qtd, n * qtd))
print("_" * 12)

