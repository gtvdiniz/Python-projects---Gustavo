import random
import pygame 
import pygame.mixer

cartela = ['avestruz', 'águia', 'burro', 'borboleta', 'cachorro', 
           'cabra', 'carneiro', 'camelo', 'cobra', 'coeho', 'cavalo', 
           'elefante', 'galo', 'gato', 'jacaré', 'leão', 'macaco', 'porco', 
           'pavão', 'peru', 'touro', 'tigre', 'urso', 'veado', 'vaca']

resultado = random.choice(cartela)

print("Bem Vindo ao jogo do bixo!!!")

valoraposta = float(input("Informe o Valor da Aposta: "))
chances = int(input("Você pode escolher até 5 chances para jogar: "))


for i in range(chances):
    if chances > 5: 
        print("Jogo terminando...")
        break
    else:
        print()

    while True:
        print(cartela)
        suaresposta = input("Digite aqui sua resposta: ").lower()
        if suaresposta in cartela:
            if suaresposta == resultado:
                print(f"Você ganhou !!! Recebeu {valoraposta * 5} reais !!!")
            else:
                print("Não.....")
            break
        else:
            print("Resposta inválida, tente novamente.")
