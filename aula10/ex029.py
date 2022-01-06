"""
Exercicio de 29
teste de velocidade acima da velocidade permitida.
identificação de faixa de velocidade excedida e calculo de multa por faixa
regra de 3
"""
from random import randint
v = randint(1, 150)  # Gera a velocidade de forma aleatoria
vp = 80              # Velocidade maxima permitida
dif = 0              # Armazena a diferença de velocidade, caso esteja acima da velocidade permitida
faixaVE = 0         # Faixada velocidade excedida

if v > 80:
    dif = v - 80
    faixaVE = (100 * dif / vp)  # Regra de 3
elif v < vp / 2:
    multa = 85
else:
    multa = 0

if faixaVE > 50:
    multa = 880
elif faixaVE > 20:
    multa = 195
elif faixaVE > 0:
    multa = dif * 7
else:
    multa = 0

print("Qual a velocidade do carro?")
print("A velodicade do carro é {}km/h".format(v))
if v > 80:
    print("Você acaba de ser multado,pois a sua velocidade foi de {}km/h ".format(v))
    print("você excedeu em {}Km/h do limite permitido e isso é {}% acima do permitido".format(dif, faixaVE))
    print("O valor da sua multa é de R${}".format(multa))
elif v < vp / 2:
    print("Você acaba de ser multado por estar abaixo da metade da velocidade permitida {}km/h".format(vp))
else:
    print("Parabens vc esta dentro do limite de velocidade")

