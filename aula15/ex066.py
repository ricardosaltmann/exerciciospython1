'''
Exercício Python 066:
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

contador = 0
soma = 0
while True:
    n = int(input("Digite um numero: [999 para parar]: "))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} e eles somam {soma}')
print("FIM")
