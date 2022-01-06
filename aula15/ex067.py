'''
Exercício Python 067:
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    num = int(input("Quer ver a tabuada de qual valor :"))
    if num >= 0:
        c = 1
        while c < 10:
            print(f"{num} x {c}  = {num * c}")
            c += 1
        print(f"{num} x {c} = {num * c}")
        print("-" * 10)
    else:
        break
print("PROGRAMA TABUADA ENCERRADO. volte sempre!")
