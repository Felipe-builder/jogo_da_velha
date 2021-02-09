from time import sleep

p1 = p2 = escolhido = pts_jogador_x = pts_jogador_o = 0


def opcao_1(c, jogadores):
    resp = " "
    while resp != "N":
        duelistas = sorteio(resp, c, jogadores)
        matriz, simbolo = construimatriz3x3()
        mostrajogo(matriz)
        while not finalizando(matriz, duelistas, jogadores):
            simbolo = jogando(matriz, simbolo)
            print('==' * 15)
            sleep(0.3)
            mostrajogo(matriz)
        print(f'FINALIZANDO A {c}ª PARTIDA!')
        sleep(1)
        print('°°' * 20)
        c += 1
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
        troca_devalores(jogadores, resp, c, trade=True)


def construimatriz3x3():
    """
    -> função cria uma traiz 3x3(lista composta) e retorna essa matriz
    para o programa principal na variavel retorno (m)
    param matriz: lista composta(matriz)
    """
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    simb = 'X'
    return matriz, simb


def mostrajogo(matriz):
    """
    -> Função mostrar a matriz
    """
    print('+---+---+---+')
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'|{matriz[linha][coluna]:^3}', end='')
        print('|')
        print('+---+---+---+')


def jogando(matriz, simb):
    """
    -> função responsável para fazer o pedido da entrada de valor pelo teclado, para assim realizar a troca de
    valores na função ;Troca().
    param simb: valor str de 'O' ou 'X' que vai ser aplicado na matriz.
    param res: valor bool que retornará da função troca().
    param pos: valor int que retornará da função validadorInt() que é aonde o Jogador do momento quer fazer
    seu lance.
    """
    res = False
    while not res:
        pos = validadorInt(f'Vai Jogar [{simb}] em qual posição? ')
        res = troca(matriz, pos, simb)
        if not res:
            if pos < 1 or pos > 0:
                print('ERRO!Digite um valor entre 1 e 9')
            else:
                print('ERRO: Lugar ocupado!')
        else:
            simb = trocajogador(simb)
        return simb


def troca(matriz, posicao, simbolo):
    """
    -> função que verifica se o valor do param: 'posicao' está dentro da matriz, caso sim, troca-se o valor
    do param: 'posicao' pelo valor do param: 'simbolo' e retorna um valor 'ok = True'
    OBS: somente haverá subistituicao se for um valor int por str, caso contrário repetirá o pedido do param:
    'posicao' retronando valor 'ok = False'.
    param posicao: é a entrada de valor int solicitada ao usuário, para que ele informe onde ele quer jogar
    param simbolo: é o valor que subistituirá o número da matriz
    param matriz: é a matriz construída inicialmente por int que ao decorrer do jogo por conta desta função
    terá elementos dela constituída por str.
    """
    ok = False
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if matriz[linha][coluna] == posicao:
                matriz[linha][coluna] = simbolo
                ok = True
    return ok


def trocajogador(simbolo):
    """
    -> Função que realiza a troca da variante: simbolo de 'X' por 'O' a cada lance realizado com sucesso.
    ou seja a cada troca realizada pela função 'troca()'
    param simbolo: é uma variavel string que vai retornar
    """
    if simbolo == 'X':
        simbolo = 'O'
    else:
        simbolo = 'X'
    return simbolo


def finalizando(matriz, duelistas, jogadores):
    """
    -> Função responsavel pela validação se a partida terminou ou não, dando um return a cada vez que é chamada
    de 'False' ou 'True' dependendo das regras de finalização do jogo da velha, por tanto quando o jogo chegar
    em uma posição vencedora ou empatadora, o retorno do param acabar = 'True' encerra o loop da partida.
    param vp_x: é o parâmetro boolean responsavel para dizer se o jogador com o simb = 'X' ou não.
    param vp_o: é o parâmetro boolean responsavel para dizer se o jogador com o simb = 'O' ou não.
    param acabar: é o parâmetro boolean que determina se a partida encerrou ou não.
    param empate: é o parâmetro boolean para defenir se houve empate para os jogadores.
    para cont: é o parâmetro que vai ajudar na lógica de definição de encerramento da partida, caso não haja
    mais casas para se jogar, este param contabilizar a possibilidades de jogadas e caso seja int(0) então
    o jogo deve ser encerrado.
    """
    global pts_jogador_o, pts_jogador_x
    empate = False
    cont = 0
    acabar, vitoria_do_x, vitoria_do_o = analises(matriz)
    atribuindo_ponto(vitoria_do_x, vitoria_do_o)
    analisando_empate(matriz, cont)
    if acabar:
        if not vitoria_do_x and not vitoria_do_o:
            pts_jogador_x += 0.5
            pts_jogador_o += 0.5
            print('Empatou')
            empate = True
    placar(vitoria_do_x, vitoria_do_o, empate, duelistas, jogadores)
    return acabar


def analisando_empate(matriz, cont):
    acabar = False
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if matriz[linha][coluna] != 'X' and matriz[linha][coluna] != 'O':
                cont += 1
    if cont == 0:
        acabar = True
    return acabar


def analises(matriz):
    acabar = vitoria_do_x = vitoria_do_o = False
    acabar, vitoria_do_x, vitoria_do_o = analisando_linha(matriz, acabar, vitoria_do_x, vitoria_do_o)
    acabar, vitoria_do_x, vitoria_do_o = analisando_coluna(matriz, acabar, vitoria_do_x, vitoria_do_o)
    acabar, vitoria_do_x, vitoria_do_o = analisando_diagonal_pri(matriz, acabar, vitoria_do_x, vitoria_do_o)
    acabar, vitoria_do_x, vitoria_do_o = analisando_diagonal_sec(matriz, acabar, vitoria_do_x, vitoria_do_o)
    return acabar, vitoria_do_x, vitoria_do_o


def analisando_linha(matriz, acabar, vitoria_do_x, vitoria_do_o):
    for linha in range(0, 3):
        if matriz[linha][0] == matriz[linha][1] == matriz[linha][2]:
            if matriz[linha][0] == 'X':
                vitoria_do_x = True
            if matriz[linha][0] == 'O':
                vitoria_do_o = True
            acabar = True
    return acabar, vitoria_do_x, vitoria_do_o


def analisando_coluna(matriz, acabar, vitoria_do_x, vitoria_do_o):
    for coluna in range(0, 3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna]:
            if matriz[0][coluna] == 'X':
                vitoria_do_x = True
            if matriz[0][coluna] == 'O':
                vitoria_do_o = True
            acabar = True
    return acabar, vitoria_do_x, vitoria_do_o


def analisando_diagonal_pri(matriz, acabar, vitoria_do_x, vitoria_do_o):
    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[0][0] == 'X':
            vitoria_do_x = True
        if matriz[0][0] == 'O':
            vitoria_do_o = True
        acabar = True
    return acabar, vitoria_do_x, vitoria_do_o


def analisando_diagonal_sec(matriz, acabar, vitoria_do_x, vitoria_do_o):
    if matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[0][2] == 'X':
            vitoria_do_x = True
        if matriz[0][2] == 'O':
            vitoria_do_o = True
        acabar = True
    return acabar, vitoria_do_x, vitoria_do_o


def atribuindo_ponto(vitoria_do_x, vitoria_do_o):
    global pts_jogador_o, pts_jogador_x
    if vitoria_do_x:
        pts_jogador_x += 1
    elif vitoria_do_o:
        pts_jogador_o += 1


def lin(tam=42):
    return '-'*tam


def titulo(msg):
    """
    -> função para definir um título com melhor estética.
    param msg: é a entrada de uma string que vai servir de cabeçalho.
    """
    print(lin())
    print(msg.center(42))
    print(lin())


def menuprincipal(lista, msg):
    """
    -> funcão a qual dá estrutura ao menu principal dando print() de cada item de uma lista por cada vez que
     realiza um laço de repetição.
    param lista: contem itens (strings) que informam ao usuário de forma interativa suas opções.
    param msg: o conteúdo principal do cabeçalho, para formar o titulo do menu de forma mais estética.
    param c: é uma variavel para definir o índice de opções baseado na quantidade de itens do 'param lista'.
    param r: é a variável solicitada ao usuário para definir sua escolha com base nas informações montada por
    esta função. retornando a variavel 'r' ao programa principal para segmento do programa.
    """
    titulo(msg)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    r = validadorInt('Opção: ')
    return r


def validadorInt(msg):
    """
    -> esta função possui o objetivo de validar informações de caracter inteiro. que a priore são usadas nas
    interações do usuário com o menu do programa ou a tabela de jogadores e o tabuleiro do jogo.
    """
    ok = False
    while not ok:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('Digite um número inteiro válido')
        else:
            ok = True
    return n


def escolhadeJogadores(jogadores):
    """
    -> esta tem por função selecionar dois jogadores, dos quais estão dentro da lista com os dados de todos os
    jogadores registrados, não podendo jogar participantes com os memos nomes. Sendo assim uma condição
    necessária para que a partida comece.
    """
    titulo('CARREGAR JOGADORES')
    global p1, p2
    if len(jogadores) == 0:
        print('NÃO HÁ JOGADORES REGISTRADO')
        return False
    for cod, j in enumerate(jogadores):
        print(f'{cod} - {j["nome"]}')
    p1, p2 = validadordejogadores(jogadores)
    jogador1 = jogadores[p1]['nome']
    jogador2 = jogadores[p2]['nome']
    ok = True
    print(f'Os jogadores Escolhido foram "{jogador1}" e "{jogador2}"')
    return ok


def validadordejogadores(jogadores):
    """
    -> esta função não permite que a escolha do jogadores seja feita de forma correta e evitando problemas é
    por tanto um validador de escolha dos jogadores como o próprio nome já diz.
    """
    while True:
        player1 = validadorInt('Escolha O primeiro Jogador: ')
        if 0 <= player1 < len(jogadores):
            print(f'O 1ª Jogador é {jogadores[player1]["nome"]}')
            break
    while True:
        player2 = validadorInt('Escolha O Segundo Jogador: ')
        if player1 == player2:
            print('ERRO! Você não pode escolher o mesmo jogador!')
        elif 0 <= player2 < len(jogadores):
            print(f'O 2ª Jogador é {jogadores[player2]["nome"]}')
            break
    return player1, player2


def sorteio(resposta, contador, jogadores):
    """
    -> tem for função sortear quem vai começar a partida e fazer as alterações ou trocas de valores do placar do
    jogador vitorioso de 'X' que na proxima rodada vai ficar com 'O':
    EX: 'Fulano' que está com 'X' e 'zero' pontos
        'Beltrano que está com 'O' e 'zero' pontos
         e caso 'Fulano' ganhe na próxima partida ele ficará
        'Fulano' jogando de 'O' está com '1' ponto
        'Beltrano' jogando de 'X' está com '0' ponto.
    """
    global pts_jogador_o, pts_jogador_x
    duelistas = ["", ""]
    print(lin())
    troca_devalores(jogadores, resposta, contador)
    if contador % 2 != 0:
        duelistas[0] = jogadores[p1]["nome"]
        duelistas[1] = jogadores[p2]["nome"]
        print(f'{duelistas[0]} vai começar a partida')
    else:
        print(f'{jogadores[p2]["nome"]} vai começar a partida')
        duelistas[0] = jogadores[p2]["nome"]
        duelistas[1] = jogadores[p1]["nome"]
    return duelistas


def troca_devalores(jogadores, resposta, contador, trade=False):
    global pts_jogador_x, pts_jogador_o
    if not trade:
        if resposta == "S":
            pts_jogador_o, pts_jogador_x = pts_jogador_x, pts_jogador_o
            jogadores[p1]['ponto'], jogadores[p2]['ponto'] = jogadores[p2]['ponto'], jogadores[p1]['ponto']
            print('Olá primeira troca.')
    elif trade:
        if resposta == 'N' and contador > 2:
            jogadores[p1]['ponto'], jogadores[p2]['ponto'] = jogadores[p2]['ponto'], jogadores[p1]['ponto']
            print('Olá segunda troca.')


def placar(vp_x, vp_o, emp, duelistas, jogadores):
    """
    -> está função altera o valor (key) 'ponto' do jogador que está dentro da lista de jogadores, caso ganhe
    +1 ponto, caso empate +0.5 para ambos jogadores. informando assim o placar temporário e posteriormente
    alterando a lista de jogadores que séra registrada em documento.
    """
    print(lin(10))
    print(f'{duelistas[0]} de X: {pts_jogador_x} pts')
    print(f'{duelistas[1]} de O: {pts_jogador_o} pts')
    if vp_x:
        jogadores[p1]['ponto'] += 1
    elif vp_o:
        jogadores[p2]['ponto'] += 1
    elif emp:
        jogadores[p1]['ponto'] += 0.5
        jogadores[p2]['ponto'] += 0.5
