from funcoes.logica import *


def inicialzaodearquivo():
    arq = 'listadejogadores.txt'
    if not arquivoExiste(arq):
        criarArquivo(arq)
    carregarArquivo(arq)
    return arq


def arquivoExiste(nome):
    """
    -> verifica se existe um arquivo para salvar os dados dos participantes do jogo. dando assim o return
    para o programa principal seguir.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    -> tal função cria o arquivo caso o return da função anterior der um return 'False'.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo "{nome}" criado com sucesso.')


def lerarquivo(nome):
    """
    -> Vai fazer a leitura do arquivo com os respectivos dados dos jogadores de uma forma mais apresentável ao
    usuário.
    """
    titulo('LISTA DE JOGADORES')
    a = open(nome, 'r')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:.<30}{dado[1]} pontos')
    a.close()


def cadastrar(arq, nome='<desconhecido>', pontos=0):
    """
    -> quando chamada essa função o usuário irá escrever dados necessário para o prosegmento do jogo.
    """
    if nome == '':
        nome = '<desconhecido>'
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro no cadastro')
    else:
        try:
            a.write(f'{nome};{pontos}\n')
        except:
            print('Houve um erro na escrita de dados')
        else:
            print(f'{nome} cadastrado com sucesso.')
            a.close()


def carregarArquivo(arq):
    """
    -> esta função servirá para criação da temporária lista de jogadores com seus respectivos dados
    que sofrerá alterações dentro do jogo, e finalmente fará o registro no documento na função 'atualizaarquivo().'
    """
    jogadores.clear()
    a = open(arq, 'r')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        jogadores.append({'nome': dado[0], 'ponto': float(dado[1])})
    a.close()


def atualizaarquivo(arq):
    """
    -> irá atualizar o arquivo com dados de todos os jogadores registrados, para ser mais preciso atualizar
    sua pontuação.
    """
    a = open(arq, 'wt')
    for x in jogadores:
        a.write(f'{x["nome"]};{x["ponto"]}\n')
    a.close()


def ranking():
    """
    -> tal função tem por objetivo organizar a lista temporária de jogadores por ordem de maior pontuador até
    o menor pontuador e apresenta-los de forma mais agradavél ao usuário.
    """
    for c in range(0, len(jogadores) - 1):
        for i in range(c, len(jogadores)):
            if jogadores[c]['ponto'] < jogadores[i]['ponto']:
                jogadores[c], jogadores[i] = jogadores[i], jogadores[c]
    titulo('RANKING DOS JOGADORES')
    for r, j in enumerate(jogadores):
        print(f'{r+1:}ª - {j["nome"]:.<30} {j["ponto"]} pts')
    print(lin())
