'''
Exercício Python 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se:
a expressão passada está com os parênteses abertos e fechados na ordem correta.
((a+b)*c) (x+y(3+2/3)*z)
'''


exp = str(input("Digite a expressão: "))
lista = []
ab = 0
fb = 0
soma = 0
for simb in exp:
    if simb == '(':
      ab += 1
    elif simb == ')':
        fb += 1
soma = ab + fb
if soma % 2 == 0:
    print("Sua expressão esta correta")
else:
    print("Sua expressão esta errada")
