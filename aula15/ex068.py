'''
Exercício Python 068:
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
print("*" * 40)
print("VAMOS JOGAR PAR OU IMPAR")
print("*" * 40)
contador = 0
while True:
    chute = int(input("Digite um valor: "))
    while True:
        pi = str(input("[PAR OU IMPAR]: ")).strip().upper()[0]
        if pi in 'IP':
            pi = pi
            break
        else:
            print("Tente outra vez,a aposta precisa ser Par ou Impar [P/I]")
    chutepc = randint(0, 10)
    soma = chutepc + chute
    if soma % 2 == 0:
        jogo = 'P'
    else:
        jogo = 'I'
    if pi == jogo:
        print("Parabens você ganhou!!!")
        contador += 1
        if contador == 1:
            print(f"Você esta com {contador} ponto")
        else:
            print(f"Você esta com {contador} pontos")
    else:
        break

if contador == 1:
    print(f"Game Over!! Você venceu {contador}  vez")
if contador > 1:
    print(f"Game Over!! Você venceu {contador}  vezes")
else:
    print('Você PERDEU!!!!')

