"""
Exercício Python 036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

v_Casa = float(input("Qual o valor do imovel a ser financiado?  R$"))
salario = float(input("Informe o Salario ? R$"))
t_Finan = int(input("Em quantos anos pretende pagar? "))

prestacao = v_Casa / (t_Finan * 12)
por = salario * 30 / 100

if prestacao > salario * 30 / 100:
    print("Para pagar a casa no valor de R${:.2f} em {} anos, a prestação ficaria em R${:.2f}".format(v_Casa,t_Finan, prestacao))
    print("Emprestimo NEGADO!")
else:
    print("Para pagar a casa no valor de R${:.2f} em {} anos, a prestação ficará em R${:.2f}".format(v_Casa, t_Finan, prestacao))
    print("Parabens, o seu emprestimo foi APROVADO!")
