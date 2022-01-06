lista = ('Lápis', 1.89,
         'Borracha', 2,
         'Caderno', 19.90,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.90,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-' * 39)