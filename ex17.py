while True: 
    print("\nBem vindo ao programa de analisar anos bissextos!")
    print("Apenas são válidos anos a partir de 4 dígitos")
    ano = int(input("Digite um número relacionado a algum ano: "))


    if len(str(ano)) < 4:
        print("Não possui 4 dígitos!")
        break




    if ano % 4 == 0: 
        print("\nO ano é bissexto!")

    else: 
        print("O ano não é bissexto!")