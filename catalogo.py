catalogo = {}

while True:
 nome = input("Entre com o nome: ")
 if nome in ('X', 'x', 'S', 's'):
  break
 
 telefone = input("Entre com o telefone: ")
 catalogo[nome]=telefone

print(f'catalogo: {catalogo}')




 