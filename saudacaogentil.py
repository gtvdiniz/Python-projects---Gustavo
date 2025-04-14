while True:
    nome = input("Qual é o Seu nome?\n")

    op = input("Qual turno você estuda? \nDigite\n[M] para Matutino\n[V] para Vespertino\n[N] para Noturno\n")
    if "M" in op or "V" in op or "N" in op:
        pass
    if op == "M" or op == 'm':
        print(f'Bom Dia {nome}!')

    elif op == "V" or op == 'v':
        print(f'Boa Tarde {nome}!')

    elif op == "N" or op == 'n':
         print(f'Bom Noite {nome}!')

    else:
        print('Digite uma opção válida')