import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'Aumentando 10%, teremos R${moeda.aumentar(p, 10, True)}')
