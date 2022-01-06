jogador = {}
dados = []
gols = []
tot = 0
while True:
    gols.clear()
    jogador["Nome"] = str(input("Nome do jogador: "))
    jogador["Partidas"] = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    if jogador["Partidas"] > 0:
        for i in range(1, jogador["Partidas"] + 1):
            gols.append(int(input(f"   Quantos gols marcados na {i}ª partida? ")))
    jogador["Gols"] = gols[:]
    jogador["Total"] = sum(gols)
    dados.append(jogador.copy())
    while True:
        opc = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opc not in 'NnSs':
            print("A resposta precisa ser S ou N")
        if opc in 'SsNn':
            break
    if opc in 'Nn':
        break
print('-=' * 40)
print(f"{'cod':<4}{'Nome':<10}{'Gols':<8}{'Total':>8}")
print('-' * 40)
cont = 0
for i, a in enumerate(dados):
    print(f"{i:<4}{a[cont]['Nome']:<10}{a['Gols']:>8.1f}")
    print('-' * 30)
    cont += 1

print(dados)'''