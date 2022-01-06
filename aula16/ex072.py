'''
Exercício Python 073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corintians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f"Os 5 primeiros colocados da tabela, são: {tabela[:5]}")
print(f"Os 4 ultimos colocados da tabela, são: {tabela[-4:]}")
print(f'O time da Chapecoense esta na {tabela.index("Chapecoense") + 1}ª possição.')
