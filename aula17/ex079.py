'''
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista = []
continuar = "S"
while True:
    v = (int(input("Digite um valor:")))
    if v not in  lista:
        lista.append(v)
    else:
        print("O valor não pode ser adicionado, poi já existe")

    continuar = str(input("Quer continuar [S/N]")).strip().upper()
    if continuar == 'N':
        break
lista.sort()
print(lista)


