print("Exercício Python 012: "
      "Faça um algoritmo que leia o preço de um produto"
      " e mostre seu novo preço, com 5% de desconto.")

preco = float(input("Digite o valor do produto"))
desconto = 0.95 # %
valor_Final = preco * desconto

print("O produto custa {} e com o desconto ele vai sair por {}".format(preco, valor_Final))


