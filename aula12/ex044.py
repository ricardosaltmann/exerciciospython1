"""
Exercício Python 044:
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""
print('{:=^40}'.format('ALTMANN'))
preco = float(input("Qual o valor das compras? R$"))

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2 x no cartão
[ 4 ] 3 x ou mais no cartão """)
e = int(input("Qual a forma de pagamento?"))
if e == 4:
    p = int(input("Em quantas vezes você pretende parcelar ?"))
    juros = (preco + (preco * 20 / 100))
    parcela = juros / p
    print("A sua compra de R${:.2f} ficou com o valor final de R${:.2f}"
          " dividido em {}X R${:.2f}".format(preco, juros, p, parcela))
else:
    if e == 1:
        total = preco - (preco * 10 / 100)
        print("Sua compra no valor de R${:.2f} vai custar R${:.2f}".format(preco, total))
    elif e == 2:
        total = preco - (preco * 5 / 100)
        print("Sua compra no valor de R${:.2f} vai custar R${:.2f}".format(preco, total))
    elif e == 3:
        parcela = preco / 2
        print("A sua compra no valor de R${:.2f} ficou com o valor e 2X R${:.2f}".format(preco, parcela))
    else:
        print("Você digitou uma opção invalida!!! tente novamente.")





