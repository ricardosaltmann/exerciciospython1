'''
Exercício Python 065:
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
soma = 0
contador = 0
continuar = 'S'
maior = 0
menor = 0
while continuar != 'N':
    n = int(input("Digite um número: "))
    continuar = str(input("Quer continuar [S/N]")).upper().strip()
    contador += 1
    soma += n
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print("A media entre todos os {} números digitados foi {}".format(contador, (soma / contador)))
print("O maior número é {} e o menor {}".format(maior, menor))




