while True:
    op = input("Quer continuar?\n [S] - sim\n [N] - não\n ")
    if op.upper() == 'S':
        pass
    elif op.upper() == 'N':
        break

    n = int(input("Digite um número inteiro qualquer: "))

    if n > 1:
        eh_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print("É um número primo\n")
        else:
            print('Não é um número primo\n')
    else:
        print('Não é um número primo\n')
