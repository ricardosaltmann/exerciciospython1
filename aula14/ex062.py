'''
Exercício Python 062:
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print("="*40)
print('{:=^40}'.format('10 TERMOS DE UMA PA'))
print("="*40)
pt = int(input("Digite o primeiro termo: "))
r = int(input("Qual a razão: "))
termo = pt
c = 1
nt = 0
mais = 10
while mais != 0:
    nt = nt + mais
    while c <= nt:
        print(termo, end=' → ')
        termo += r
        c += 1
    print("Pausa")
    mais = int(input("Quantos termos mais vc quer mostrar?"))
print("Progressão finalizada com {} termos  mostrados".format(nt))

