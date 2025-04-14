n1 = float(input("Digite o preço do primeiro produto: "))
n2 = float(input("Digite o preço do segundo: "))
n3 = float(input("Digite o preço do terceiro: "))

if n1 < n2 and n1 < n3:
     print(f'O produto que você deve comprar é o com valor: {n1}')

elif n1 > n2 and n2 < n3:
      print(f'O produto que você deve comprar é o com valor: {n2}')

elif n1 > n3 and n2 > n3:
      print(f'O produto que você deve comprar é o com valor: {n3}')