"""
Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('='*40)
print('{:=^40}'.format('BANCO ALTMANN'))
print('='*40)
while True:
    saque = int(input("Qual o valor você quer sacar? R$"))
    u = saque // 1 % 10         #R$1.00
    d = saque // 10 % 10        #R$10.00
    c = saque // 100 % 10       #R$50.00
    m = saque // 1000 % 100     #R$100.00

    if m > 0:
        n100 = (m * 1000) / 100
        print(f"Total de {n100:.0f} cedulas de R$100,00")
    if c > 0:
        n50 = (c * 100) / 50
        print(f"Total de {n50:.0f} cedulas de R$50,00")
    if d > 0:
        print(f"Total de {d} cedulas de R$10,00")
    if u > 0:
        if u >= 5:
            n1 = u - 5
            n5 = 1
            print(f"Total de {n5} cedulas de R$5,00")
            if n1 >0:
                print(f"Total de {n1} cedulas de R$1,00")
        else:
            print(f"Total de {u} cedulas de R$1,00")
    break
print("Volte sempre ao banco Altmann, Tenha um bom dia")
