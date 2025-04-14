vogal = 'aeiou'
consoante = 'bcdfghjklmnpqrstvwxyz'
while True:
    letra = str(input("Digite uma letra: "))

    if letra in vogal:
        print("Essa é uma vogal!")
    
    elif letra in consoante:
        print("Essa é uma consoante!")

    else:
        print('Opção inválida!!!')
        break