"""
Exercício Python 053:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

nome = str(input("Informe uma Frase ou nome: ")).strip().upper() #pegar frase em string, sem espaços e caixa alta
palavras = nome.split()       #Depois separar a frase em palavras
junto = ''.join(palavras)     #juntar usando join e com o '' para indicar o caracter que vai juntar exe '=' ou '-' ou '' para juntar
inverso = ''                  #criar variavel vazia para receber a palavra invertida
for letra in range(len(junto) -1, -1, -1 ):  #Fazer um for e armazenando em letra pegar tamanho com len e usar - 1 para inverter
    inverso += junto[letra]                  #Inverso recebe dados do junto que recebeu letra que é a informação invertida
print(junto, inverso)

if junto == inverso:
    print("Temos um palindramo")
else:
    print("A frase digitada não é um palindramo")



nome = str(input("Informe uma Frase ou nome: ")).strip().upper() #pegar frase em string, sem espaços e caixa alta
palavras = nome.split()       #Depois separar a frase em palavras
junto = ''.join(palavras)     #juntar usando join e com o '' para indicar o caracter que vai juntar exe '=' ou '-' ou '' para juntar
inverso = junto[::-1]
print(junto, inverso)

if junto == inverso:
    print("Temos um palindramo")
else:
    print("A frase digitada não é um palindramo")



