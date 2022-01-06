import emoji
from random import randint
from time import sleep

chutepc = randint(0, 2)
print(chutepc)
print("""Escolha a sua opção: 
[ 0 ] pedra 👊
[ 1 ] PAPEL 📜
[ 2 ] TESOURA ✂
""")
chute = int(input("Qual será a sua jogada?"))
if chute < 0:
    print("Jogada so pode ser 1 2 ou 3, tente outra vez")
elif chute > 2:
    print("Jogada so pode ser 1 2 ou 3, tente outra vez")
else:
    sleep(0.5)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    print('-=' * 12)

    if chute == 0 and chutepc == 1 or chute == 1 and chutepc == 2 or chute == 2 and chutepc == 0:
        if chutepc == 0:
            chutepc = "PEDRA"
        elif chutepc == 1:
            chutepc = "PAPEL"
        elif chutepc == 2:
            chutepc = "TESOURA"
        if chute == 0:
            chute = "PEDRA"
        elif chute == 1:
            chute = "PAPEL"
        else:
            chute = "TESOURA"
        print("Computador jogou {}".format(chutepc))
        print("Jogador jogou {}".format(chute))
        print('-=' * 12)
        print("Jogador PERDEU")

    elif chute == 0 and chutepc == 2 or chute == 1 and chutepc == 0 or chute == 2 and chutepc == 1:
        if chutepc == 0:
            chutepc = "PEDRA"
        elif chutepc == 1:
            chutepc = "PAPEL"
        elif chutepc == 2:
            chutepc = "TESOURA"
        if chute == 0:
            chute = "PEDRA"
        elif chute == 1:
            chute = "PAPEL"
        else:
            chute = "TESOURA"
        print("Computador jogou {}".format(chutepc))
        print("Jogador jogou {}".format(chute))
        print('-=' * 12)
        print("Jogador VENCEU")
    else:
        if chutepc == 0:
            chutepc = "PEDRA"
        elif chutepc == 1:
            chutepc = "PAPEL"
        elif chutepc == 2:
            chutepc = "TESOURA"
        if chute == 0:
            chute = "PEDRA"
        elif chute == 1:
            chute = "PAPEL"
        else:
            chute = "TESOURA"
        print("Computador jogou {}".format(chutepc))
        print("Jogador jogou {}".format(chute))
        print('-=' * 12)
        print("O jogo EMPATOU")
