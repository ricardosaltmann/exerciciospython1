'''
Exercício Python 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogador4': randint(1, 6)
           }

print("Valores sorteados:")
for j, v in sorteio.items():
    print(f"{j} tirou {v} no dado.")
    sleep(1)

ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('-=' * 40)
print('{:=^30}'.format('RANKING DOS JOGADORES'))

print("metodo 1")
for i, v in enumerate(ranking):
    print(f"{i}º lugar: {v[0]} com {v[1]}")
    sleep(1)


print("metodo 2 Ricardo")
contador = 1
for k, v in ranking:
    print(f"{contador}º lugar: {k} com {v}")
    contador +=1
    sleep(1)