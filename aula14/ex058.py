'''
Exercício Python 058:
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
'''
from random import randint
chute = randint(0, 10)
contador = 0
print("""Sou seu computador...
Acabei de pensar em um número de 0 a 10.
sera que vccê consegue adivinhar qual foi ?
""")
acertou = False
while not acertou:
    palpite = int(input("Qual o seu palpite ? "))
    contador += 1
    if palpite == chute:
        acertou = True
    else:
        if palpite < chute:
            print("Mais... Tente outra vez")
        elif palpite > chute:
            print("Menos... tente outra vez")
print("Acertou com {} tentativas. Parabens".format(contador))