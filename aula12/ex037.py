"""
Exercício Python 037:
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

n = int(input("Digite o número a ser convertido: "))

print("Para qual base esse número será convertido?")
print("[ 1 ] para Binário")
print("[ 2 ] para octal")
print("[ 3 ] para hexadecimal")
e = int(input("Escolha uma opção:"))
if e == 1:
    b = format(n, "b")
    print("O número {} convertido para Binário é {}".format(n, b))
elif e == 2:
    o = format(n, "o")
    print("O número {} convertido para Octal é {}".format(n, o))
else:
    h = format(n, "x")
    print("O número {} convertido para Hexadecimal é {}".format(n, h))


"""
Tipo de formatação	Papel
=	Coloca o sinal na posição mais à esquerda
b	Converte o valor em binário equivalente
o	Converte o valor para o formato octal
x	Converte o valor para o formato Hex
d	Converte o valor dado em decimal
E	Formato científico, com um E em maiúsculas
X	Converte o valor para o formato Hex em maiúsculas
"""