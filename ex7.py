n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
n3 = float(input("Digite mais outro número: "))

if n1 > n2 and n1 > n3 and n3 > n2 :
    print(f'O maior número é {n1} e o menor é {n2}')

elif n1 > n2 and n1 > n3 and n3 < n2 :
    print(f'O maior número é {n1} e o menor é {n3}')

elif n1 < n2 and n2 > n3 and n1 < n3 :
     print(f'O maior número é {n2} e o menor é {n1}')

elif n1 < n2 and n2 > n3 and n1 > n3 :
     print(f'O maior número é {n2} e o menor é {n3}')

elif n1 < n3 and n2 < n3 and n1 < n2:
      print(f'O maior número é {n3} e o menor é {n1}')

elif n1 < n3 and n2 < n3 and n1 > n2:
      print(f'O maior número é {n3} e o menor é {n2}')
