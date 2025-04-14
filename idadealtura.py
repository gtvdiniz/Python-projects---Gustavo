idade = []
altura = []
i = 0 
a = 0 

for i in range(5):
    i = int(input("Digite a Idade: "))
    idade.append(i)
   

for a in range(5):
    a = float(input("Digite a Altura: "))
    altura.append(a)
    
print(f' a ordem original é: {idade}')
print(f' ordem original é: {altura}')
idade.reverse()
print(f'a ordem inversa é : {idade}')
altura.reverse()
print(f'a ordem inversa é : {altura}')

