while True:
    op = int(input("\n[0] - Rodar programa\n[1] - Sair do programa\n"))


    if op == 0:
     pass
    elif op == 1: 
        break


    data = input("Informe a data no formato dd/mm/aaaa\n:")
    dia, mes, ano = data.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)


    if ano < 1930 and ano > 2100:
        print('Data inválida')

    elif ano % 4 == 0:
     if mes == 2 and dia > 29:
        print('Data inválida')
     else: print("Data válida")

    elif dia > 31 and mes == 1 or dia > 28 and mes == 2 or dia > 31 and mes == 3 or dia > 30 and mes == 4 or dia > 31 and mes == 5 or dia > 30 and mes == 6 or dia > 31 and mes == 7 or dia > 31 and mes == 8 or dia > 30 and mes == 9 or dia > 31 and mes == 10 or dia > 30 and mes == 11 or dia > 31 and mes == 12:
        print("Data inválida")

    else: print("Data válida")

