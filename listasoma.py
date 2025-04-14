lista = []
n = 0 
produto = 1

for n in range(15):
    n = int(input("Digite um valor: "))
    lista.append(n)
  
for item in lista:
    produto *= item
    

print(lista)
print(f'soma = {sum(lista) }')
print(f'mínimo = {min(lista) }')
print(f'máximo = {max(lista) }')
print(f'produto = {produto}')






