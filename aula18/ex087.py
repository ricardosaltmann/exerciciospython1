"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = ster = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para {l} e {c}: "))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print("=-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{[matriz[l][c]]}", end='')
    print()
for c in range(0, 3):
    if matriz[1][c] == 0:
        maior += matriz[1][c]
    elif matriz[1][c] > maior:
        maior += matriz[1][c]



ster = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(maior)
print(f"A soma dos valores par é: {spar}")
print(f"A soma dos valores da 3ª coluna é: {ster}")




