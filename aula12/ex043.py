"""
Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
Calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua algura em cm:")) / 100
imc = peso / (altura ** 2)
if imc <= 18.5:
    print("O seu IMC é {:.1f} ".format(imc))
    print("Você esta abaixo do pelo normal")
elif imc <= 25:
    print("O seu IMC é {:.1f} ".format(imc))
    print("PARABÉNS Você esta com o peso ideal! ")
elif imc <= 30:
    print("O seu IMC é {:.1f} ".format(imc))
    print("Cuidado você já esta com sobrepeso")
elif imc <= 40:
    print("O seu IMC é {:.1f} ".format(imc))
    print("Alerta você já esta OBESO!!")
else:
    print("O seu IMC é {:.1f} ".format(imc))
    print("Procure um medico você esta com Obesidade mórbida")
