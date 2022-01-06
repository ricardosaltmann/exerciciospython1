print("Exercício Python 008: Escreva um programa que leia um valor em metros"
      " e o exiba convertido em centímetros e milímetros.")

print("Vamos iniciar o calculo da metragem da parede")
altura = int(input("Digite a altura da parede"))
largura = int(input("Ótimo, agora eu preciso da largura"))
m = altura * largura
c = m * 100
mil = m * 1000
print("A sua parede tem {}m², {} centimetros e {} milimetros".format(m, c, mil))
