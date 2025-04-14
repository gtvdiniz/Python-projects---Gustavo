print("Programa Triângulo")

l1 = float(input("Informe os valores do lado 1 do triângulo: "))

l2 = float(input("Informe os valores do lado 2 do triângulo: "))

l3 = float(input("Informe os valores do lado 3 do triângulo: "))


soma2lados = l1 + l2 

soma2lados1 = l1 + l3 

soma2lados2 = l2 + l3 


if soma2lados > l3 and soma2lados1 > l2 and soma2lados2 > l1: 
    print("É um triângulo!")

    if l1 == l2 == l3: 
         print("O triângulo é equilátero!")

    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1: 
        print("O triângulo é isósceles!")

    else: 
        print("O triângulo é escaleno!")

else: 
    print("Não é um triângulo")

