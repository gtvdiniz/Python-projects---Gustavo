vogal = 'AEIOUaeiou'
consoante = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'

l = input("Digite uma letra:")

if l in vogal: 
    print(f'A letra {l} é uma vogal')

elif l in consoante: 
    print(f'A letra {l} é uma consoante')

else: 
    print("Caractere inválido")