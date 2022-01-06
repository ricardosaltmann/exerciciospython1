'''
Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavra = ('Caderno', 'Monitor', 'Mangueira', 'Celular', 'Garrafa', 'Prateleira',
           'Computador', 'Armario', 'Janela', 'Suporte', 'Microfone', 'Chinelo',
           'Lareira', 'Calculadora', 'Carro', 'Lambreta', 'pneumoultramicroscopicossilicovulcanoconiótico')
for l in palavra:
    print(f"\nNa palavra {l.upper()}, temos as vogais:", end=' ')
    for letra in l:
        if letra in 'aeiou':
            print(letra.lower(), end=' ')
