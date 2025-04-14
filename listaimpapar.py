todos = []
par = []
impar = []

n = 0 

for n in range(20):
    n = int(input("Digite um valor: "))
    todos.append(n)
    
    if n % 2 == 0: 
        par.append(n)

    else: 
        impar.append(n)

print(todos)
print(par)
print(impar)