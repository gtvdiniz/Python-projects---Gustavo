n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
n3 = float(input("Digite mais outro número: "))

#n1 é o maior, n3 o segundo e n2 o menor
if n1 > n2 and n1 > n3 and n3 > n2 :
    print(f'A ordem é {n1}, {n3}, {n2}')

#n1 é o maior, n2 o segundo e n3 o menor
elif n1 > n2 and n1 > n3 and n3 < n2 :
    print(f'A ordem é {n1}, {n2}, {n3}')

#n2 é o maior, n3 o segundo e n1 o menor
elif n1 < n2 and n2 > n3 and n1 < n3 :
    print(f'A ordem é {n2}, {n3}, {n1}')

#n2 é o maior, n1 o segundo e n3 o menor
elif n1 < n2 and n2 > n3 and n1 > n3 :
    print(f'A ordem é {n2}, {n1}, {n3}')

#n3 é o maior, n2 o segundo e n1 o menor
elif n1 < n3 and n2 < n3 and n1 < n2:
      print(f'A ordem é {n3}, {n2}, {n1}')

#n3 é o maior, n1 o segundo e n2 o menor
elif n1 < n3 and n2 < n3 and n1 > n2:
    print(f'A ordem é {n2}, {n3}, {n1}')


