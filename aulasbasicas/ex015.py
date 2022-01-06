print("Exercício Python 015:"
      "Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado"
      " e a quantidade de dias pelos quais ele foi alugado. "
      "Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado")
qi = float(input("Digite o km inicial"))
qf = float(input("Digite a km final"))
dias = int(input("Quantos dis o carro foi alugado"))
diaria = 60
km = 0.15
kmtotal = qf - qi
vdiaria = dias * diaria
vkm = km * kmtotal

print("Foram percorridos {}Km em {}dias".format(kmtotal, dias))
print("Custo da quilometragem R${}".format(vkm))
print("O valor da conta é de R${}".format(vkm + vdiaria))


