lista = []
while True: 
    gen = str(input("Digite um caracter\nF - Feminino\nM - Masculino\nN - Neutro\n"))
    quantidadef = lista.count('feminino')
    quantidadem = lista.count('masculino')
    quantidadei = lista.count('gênero inválido')
    quantidaden = lista.count('neutro')

    if gen == 'x' or gen == 'X':
        print(f'Feminino:{quantidadef}\nMasculino:{quantidadem}\nNeutro:{quantidaden}\nGênero Inválido:{quantidadei}\n')
        break

    elif gen == 'F' or gen == 'f':
        lista.append('feminino')

    elif gen == 'M' or gen == 'm':
        lista.append('masculino')
    
    elif gen == 'N' or gen == 'n':
        lista.append('neutro')

    else:
        lista.append('gênero inválido')


