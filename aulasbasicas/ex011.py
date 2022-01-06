print("Exercício Python 011:"
    " Faça um programa que leia a largura e a altura de uma parede em metros,"
    " calcule a sua área e a quantidade de tinta necessária para pintá-la "
    ",sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.")

print("Vamos iniciar o calculo da metragem da parede")
altura = int(input("Digite a altura da parede"))
largura = int(input("Ótimo, agora eu preciso da largura"))
m = altura * largura
c = m * 100
mil = m * 1000
print("A sua parede tem {}m², {} centimetros e {} milimetros".format(m, c, mil))

latas = m / 2
print(f"Para pintar esta parede, você vai precisar de {latas} latas de tinta")