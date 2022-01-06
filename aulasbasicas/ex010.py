print("Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira"
      " e mostre quantos dólares ela pode comprar.")

carteira = int(input("Quanto vc tem na carteira"))
dolar = 5.61
real = 1
total = ((real / dolar) * carteira)
print("Você pode comprar ${} Dolares".format(total))
