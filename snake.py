import pygame 
import random 

#Display
pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
roxa = (153, 51, 153)
azul = (0, 0, 255)

#Cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15 


def gerar_comida():
    comida_x = (random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado))  * float(tamanho_quadrado)
    comida_y = (random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, azul, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, roxa)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0

    return velocidade_x, velocidade_y

#Jogo
def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2 

    velocidade_x = 0 
    velocidade_y = 0 

    tamanho_cobra = 1 
    pixels = []


    comida_x, comida_y = gerar_comida()
   

    while not fim_jogo:
        tela .fill(verde)

        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True 
            elif evento.type == pygame. KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)



        #desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)


        #atualizar posição da cobrinha
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True




        x += velocidade_x
        y += velocidade_y

        

        #desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #cobrinha bateu no próprio corpo
        for pixel in pixels[:-1]: 
            if pixel == [x, y]:
                fim_jogo = True
        
        desenhar_cobra(tamanho_quadrado, pixels)
       
       
       
       
        desenhar_pontuacao(tamanho_cobra - 1)







        #atualizar tela 
        pygame.display.update()



        if abs(x - comida_x) < tamanho_quadrado and abs(y - comida_y) < tamanho_quadrado:

            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()


        relogio.tick(velocidade_jogo)





rodar_jogo() 
pygame.quit()