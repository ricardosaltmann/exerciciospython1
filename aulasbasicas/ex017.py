import math

co = float(input("Digite o cateto oposto: \n"))
ca = float(input("Digite o cateco adjacente: \n"))
hi = math.hypot(co, ca)
hi1 = (co ** 2 + ca ** 2) ** (1/2)
print("A hypotenusa é {:.2f}".format(hi))
print("A hypotenusa com formula matematica {:.2f}".format(hi1))
