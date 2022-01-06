from random import randint
from time import sleep
lista = ("PEDRA", "PAPEL", "TESOURA")
cpc = randint(0, 2)
print("""Escolha a sua opção: 
[ 0 ] pedra 👊
[ 1 ] PAPEL 📜
[ 2 ] TESOURA ✂""")
chute = int(input("Qual será a sua jogada?"))
if chute != 0 or 1 or 2:
    print("Jogada so pode ser 1 2 ou 3, tente outra vez")
else:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    print('-=' * 12)

    if chute == 0 and cpc == 1 or chute == 1 and cpc == 2 or chute == 2 and cpc == 0:
        print("Jogador VENCEU!!")
    elif chute == 0 and cpc == 2 or chute == 1 and cpc == 0 or chute == 2 and cpc == 1:
        print("Jogador VENCEU!!")
    else:
        print("O jogo EMPATOU!!")
print('-=' * 12)
print("Computador jogou {}".format(lista[cpc]))
print("Jogador jogou {}".format(lista[chute]))
