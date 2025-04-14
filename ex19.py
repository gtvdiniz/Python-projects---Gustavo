while True: 
    n = int(input("Escreva um número inteiro menor que 1000: "))

    if n >= 1000: 
        print("Inválido!")

    else: 
        pass


    unidade = n % 10 

    n = (n - unidade)/10

    dezena = n % 10
    
    n = (n - dezena)/10
    centena = n

    dezena = int(dezena)
    centena = int(centena)


    
    print(f'Possui {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')

    