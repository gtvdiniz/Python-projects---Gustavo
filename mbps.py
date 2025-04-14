while True: 
    op = input("Você deseja sair do programa?\nse sim digite [S]\nSe não digite qualquer caracter\n")
    
    if op == 'S' or op == 's':
        break

    else:
        print("Programa rodando...\n")

    
    
    
    
    velocidade_arquivo = float(input("Informe o valor do arquivo em MBPS: "))

    velocidadegiga = velocidade_arquivo / 8

    arquivo = float(input("Informe o tamanho do arquivo: "))

    tempo_download = arquivo / velocidadegiga

    print(f'são necessários {tempo_download} segundos\n')

 
