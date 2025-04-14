def ExercicioDolar():

    valorD = float(input("Coloque quantos dólares você tem:"))
    cotacao = float(input("Coloque a cotação do dólar:"))
    Reais = valorD * cotacao
    print("Escolha a opção: [1]CONVERTER [2]SAIR")


    op = int(input())

    if op == 1: 
        print("O valor em reais é", Reais)
    elif op == 2: 
        print()
    else : 
        return op
  

    
ExercicioDolar()

