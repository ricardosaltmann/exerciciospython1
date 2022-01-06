"""
Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: \033[0;33:44mREPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
n1 = float(input("Digite a nota de Matematica:"))
n2 = float(input("Digite a nota de Portugues"))

if (n1 + n2) / 2  >= 7.0:
    print("Parabens você foi APROVADO, a sua nota foi {:.2f}".format((n1 + n2) / 2))
elif (n1 + n2) / 2 < 5.0:
    print("Infelismente você foi REPROVADO, a sua nota foi {:.2f}".format((n1 + n2) / 2))
else:
    print("Sua nota é {:.2f}, e você esta de RECUPERAÇÃO".format((n1 + n2) / 2))
