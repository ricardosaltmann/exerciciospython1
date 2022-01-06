'''
Exercício Python 061:
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print("="*40)
print('{:=^40}'.format('10 TERMOS DE UMA PA'))
print("="*40)
pt = int(input("Digite o primeiro termo: "))
r = int(input("Qual a razão: "))
c = 1
termo = pt
while c <= 10:
    print(termo, end=' → ')
    termo += r
    c += 1
print("FIM")



