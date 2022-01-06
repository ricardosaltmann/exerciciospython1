from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print("arquivo não encontrado")
    criarArquivo(arq)
while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Opção 3')
        lerArquivo(arq)
    elif resposta == 4:
        print('Saindo do sistema ... ate logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção valida!\033[m')
    sleep(2)
