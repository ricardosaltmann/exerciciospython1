"""
Exercício Python 101:
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem
 voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: É menor que 16 anos e ainda não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O voto é facultativo.'
    else:
        return f'Com {idade} anos: O voto é Obrigatorio.'




nasc = int(input("Em que ano você nasceu?: "))
print(voto(nasc))