'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    c = str(input("Quer continuar ? [S/N]: ")).strip().upper()[0]
    while c not in 'SsNn':
        print("Digite S para Sim ou N para Não")
        c = str(input("Quer continuar ? [S/N]: ")).strip().upper()[0]
    if c in 'Nn':
        break

lista.sort(reverse=True)
print("-=" * 40)
print(f"Foram digitados {len(lista)} números")
print(f"Os valores digitados foram {lista}")
if 5 in lista:
    print("O número 5 foi digitado e esta na lista!")
else:
    print("O número 5 não foi encontrado na lista")

