from time import sleep


def contagem(i, f, r):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param r: razao da contagem
    :return: sem retorno
    """
    if r < 0:
        r *= -1
    if r == 0:
        r = 1
    print('-=' * 30)
    print(f"Contagem de {i} até {f} de {r} em {r}")
    sleep(2)

    if i < f:
        while i <= f:
            print(f'{i} ', end='')
            i += r
            sleep(0.5)
        print("FIM!")
    elif i > f:
        while f <= i:
            print(f'{i} ', end='')
            i -= r
            sleep(0.5)
        print("FIM!")


