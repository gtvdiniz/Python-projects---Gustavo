catalogo = {}
valores = []

while True:
 nome = input("Entre com o nome: ")
 if nome in ('X', 'x', 'S', 's'):
  break
 
 telefone = input("Entre com o telefone: ")
 valores.append(telefone)
 email = input("Entre com o email: ")
 valores.append(email)


 catalogo[nome]=valores


print(f'catalogo: {catalogo}')


while True:
 nome = input("Entre com o nome: ")
 if nome in ('X', 'x', 'S', 's'):
  break
 
 print(f' o telefone do {nome} é {catalogo(nome)}')