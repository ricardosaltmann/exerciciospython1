def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[0:31mERRO! Digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\33[0:31mO usuário optou por não digitar um número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('\33[0:31mERRO! Digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\33[0:31mO usuário optou por não digitar um número.\033[m')
            return 0
        else:
            return n2


n = leiaInt('Digite um número: ')
n2 = leiaFloat("Digite um Real")
print(f'Valor digitado foi 0 {n} e o real foi {n2}')