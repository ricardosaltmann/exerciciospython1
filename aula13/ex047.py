"""
Exercício Python 047:
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
for c in range(1, 51,):
    if c % 2 == 0:
        print(c, end=' ')
print("Fim do metodo usando o processador para o laço impar o par e so pegando o par")

for c in range(2, 51, 2):
    print(c, end=' ')
print("Fim do metodo usando o processador so para o par MELHOR")

