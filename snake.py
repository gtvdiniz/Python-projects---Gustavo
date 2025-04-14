import pygame
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definindo o tamanho da tela
largura_tela = 600
altura_tela = 400

# Criando a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio
clock = pygame.time.Clock()

# Definindo as variáveis da cobrinha
largura_cobra = 10
altura_cobra = 10
velocidade_cobra = 15

# Fontes
fonte_pontos = pygame.font.SysFont("bahnschrift", 25)

# Função para exibir a pontuação
def nossa_pontuacao(pontos):
    valor = fonte_pontos.render("Pontuação: " + str(pontos), True, preto)
    tela.blit(valor, [0, 0])

# Função para desenhar a cobrinha
def nossa_cobra(largura_cobra, altura_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], largura_cobra, altura_cobra])

# Função para o jogo
def jogo():
    fim_de_jogo = False
    ganhou = False

    # Posições iniciais da cobrinha
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2
    x_cobra_mudanca = 0
    y_cobra_mudanca = 0

    # Lista da cobrinha
    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    comida_x = round(random.randrange(0, largura_tela - largura_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - altura_cobra) / 10.0) * 10.0

    # Pontuação
    pontos = 0

    # Loop principal do jogo
    while not fim_de_jogo:

        # Checando se o jogador perdeu
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobra_mudanca = -largura_cobra
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobra_mudanca = largura_cobra
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobra_mudanca = -altura_cobra
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobra_mudanca = altura_cobra
                    x_cobra_mudanca = 0

        # Se a cobrinha sair da tela, o jogo acaba
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            fim_de_jogo = True

        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca
        tela.fill(azul)

        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, largura_cobra, altura_cobra])

        # Atualiza a lista da cobrinha
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Se a cobrinha colidir com ela mesma, o jogo acaba
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                fim_de_jogo = True

        nossa_cobra(largura_cobra, altura_cobra, lista_cobra)
        nossa_pontuacao(pontos)

        pygame.display.update()

        # Se a cobrinha comer a comida, aumenta o comprimento e a pontuação
        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = round(random.randrange(0, largura_tela - largura_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - altura_cobra) / 10.0) * 10.0
            comprimento_cobra += 1
            pontos += 10

        # Controlando a velocidade da cobrinha
        clock.tick(velocidade_cobra)

    # Mensagem de fim de jogo
    if fim_de_jogo:
        pygame.quit()
        quit()

# Rodando o jogo
jogo()
