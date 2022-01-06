'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input("Primeiro Valor:"))
n2 = int(input("Segundo Valor:"))
sair = False
while not sair:
    opcao = int(input('''    [ 1 ] somar 
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa 
>>>>> Qual é a sua opção? '''))
    if opcao == 1:
        soma = n1 + n2
        print("O Resultado da Soma de {} + {} é {}".format(n1, n2, soma))
    elif opcao == 2:
        m = (n1 * n2)
        print("O Resultado da Multiplicaçâo de {} X {} é {}".format(n1, n2, m))
    elif opcao == 3:
        if n1 > n2:
            print("Entre {} e {} o maior é {}".format(n1, n2, n1))
        else:
            print("Entre {} e {} o maior é {}".format(n1, n2, n2))
    elif opcao == 4:
        print("Informe os números novamente:")
        n1 = int(input("Primeiro Valor:"))
        n2 = int(input("Segundo Valor:"))
        print(">>>>> Qual é a sua opção?")
    elif opcao == 5:
        sair = True
        print("Finalizando......")
    else:
        print("\033[31mOpção invalida. tente novamente\033[m")
    sleep(2)
    print("=-="*12)
print("Fim do programa")
