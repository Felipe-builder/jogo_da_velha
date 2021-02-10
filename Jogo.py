"""
Este é o programa principal que irá importar funções de outras bibliotecas, para execução corretamente
do jogo da velha.
"""
from funcoes.dados.banco_de_dados import *
from funcoes.logica import *

c, r = 1, 0
arq = inicialzaodearquivo()
jogadores = carregar_arquivo(arq)
while r != 4:
    r = menuprincipal(['Criar Jogador', 'Carregar Jogadores já Criado', 'Ranking', 'Sair do Jogo'], 'MENU PRINCIPAL')
    if r == 1:
        jogadores = opcao1_menuprincipal(arq)
    elif r == 2:
        opcao2_menuprincipal(jogadores, arq, c)
    elif r == 3:
        ranking(jogadores)
    elif r == 4:
        titulo('JOGO FINALIZADO')
    else:
        print('\033[31mDigite um valor entre 1 e 4\033[m')

