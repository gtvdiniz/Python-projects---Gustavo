jogador = 'X'
tab = [[' ']*3, [' ']*3, [' ']*3]
def ImprimirTabuleiro():
    print("_________")
    for i in range(3):
        print(f'{tab[i][0]} | {tab[i][1]} | {tab[i][2]}')
        print("_________")

def jogada(letra):
    while True:
        n = int(input("Entre com a Linha: "))
        n2 = int(input("Entre com a Coluna: "))
        
        if tab[n][n2] == ' ':
            tab[n][n2] = letra
            break

        else: 
            print("Posição inválida!!!")
            
vencedor = False
for i in range(9):
    ImprimirTabuleiro()
    if i % 2 == 0:
        jogada('X')
    else: 
        jogador = 'O'
        jogada('O')

    fimdejogo =  tab[0][0] == jogador and tab[0][1] == jogador  and tab[0][2] == jogador or tab[1][0] == jogador  and tab[1][1] == jogador  and tab[1][2] == jogador  or tab[2][0] == jogador  and tab[2][1] == jogador  and tab[2][2] == jogador  or tab[0][0] == jogador  and tab[1][0] == jogador  and tab[2][0] == jogador  or tab[0][1] == jogador  and tab[1][1] == jogador  and tab[2][1] == jogador  or tab[0][2] == jogador  and tab[2][1] == jogador  and tab[2][2] == jogador  or tab[0][0] == jogador  and tab[1][1] == jogador  and tab[2][2] == jogador  or tab[2][0] == jogador  and tab[1][1] == jogador  and  tab[0][2] == jogador 
    if fimdejogo:
        ImprimirTabuleiro()
        print(f"jogador {jogador} venceu!!!!")
        vencedor = True
        break
    if not vencedor:
        print("Deu Velha")

       
   
    
   







    

    


    

    
    


    

        
        



