nome = str(input("Digite seu nome: \n")).strip().upper()
if nome == "RICARDO":
    print("Que nome bonito")
print("Bom dia {} prazer em conhecelo".format(nome))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print(f"A sua media foi {m}")
if m >= 6:
    print(f"Parabens {nome} você passou de ano")
else:
    print("Que pena, você precisa estudar mais")
