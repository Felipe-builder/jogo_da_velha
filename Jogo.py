"""
Este é o programa principal que irá importar funções de outras bibliotecas, para execução corretamente
do jogo da velha.
"""
from funcoes.dados.banco_de_dados import *

c, r = 1, 0
arq = inicialzaodearquivo()
jogadores = carregarArquivo(arq)
while r != 4:
    r = menuprincipal(['Criar Jogador', 'Carregar Jogadores já Criado', 'Ranking', 'Sair do Jogo'], 'MENU PRINCIPAL')
    if r == 1:
        titulo('CRIANDO JOGADORES')
        nome = str(input(f'Nome do Jogador: ')).strip()
        cadastrar(arq, nome, 0)
        jogadores = carregarArquivo(arq)
    elif r == 2:
        if len(jogadores) < 2:
            print('Você precisa criar mais Jogador')
        else:
            pronto = escolhadeJogadores(jogadores)
            if pronto:
                op = menuprincipal(['Continuar?', 'Voltar?'], 'Começar a Partida')
                if op == 1:
                    opcao_1(c, jogadores)
                    atualizaarquivo(arq, jogadores)
    elif r == 3:
        ranking(jogadores)
    elif r == 4:
        titulo('JOGO FINALIZADO')
    else:
        print('\033[31mDigite um valor entre 1 e 4\033[m')
lerarquivo(arq)
