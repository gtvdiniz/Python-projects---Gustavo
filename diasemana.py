diasemana = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sábado'}
while True: 
    op = int(input("Escreva um número: "))

    if op in diasemana:
        print(f"{diasemana[op]}\n")
    
    elif op == 0:
        break

    else: print("Opção inválida")