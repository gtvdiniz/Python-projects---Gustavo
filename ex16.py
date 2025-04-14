
while True:
    a = int(input("Informe o valor de a: "))

    if a == 0: 
        print("Não é uma equação do segundo grau")
        break


    b = int(input("Informe o valor de b: "))

    c = int(input("Informe o valor de c: "))


    delta = b**2 - (4*a*c)

    raizpozetivo = (b + delta)/2*a

    raiznegativo = (b - delta)/2*a

    if delta < 0: 
        print("A equação não possui raízes!")
        break

    elif delta == 0: 
        print("A equação possui uma raíz!")
        print(raizpozetivo)

    else: 
        print(f"As raízes são {raizpozetivo} e {raiznegativo}")

