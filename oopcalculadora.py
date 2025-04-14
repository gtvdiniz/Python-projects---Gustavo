class Calculadora:
    def __init__(self):
        pass


    def adicionar(self, x, y):
        return x + y
    
    def subtrair(self, x, y):
        return x - y

    def multiplicar(self,x, y):
        return x * y
    
    def dividir(self, x, y):
     if y != 0:
        return x / y
     else:
        print("Erro: Divisão por zero não é permitida.")
        return None

        

while True: 
    oper = input("Entre com a operação: ")
    if oper in ('+', '-', '*', '/'):
     break

calc = Calculadora()

a = int(input('entre com a: '))
b = int(input('entre com b: '))


if oper == '+':
    print(f'{calc.adicionar(a, b)}')

elif oper == '-':
    print(f'{calc.subtrair(a, b)}')

elif oper == '*':
    print(f'{calc.multiplicar(a, b)}')

elif oper == '/':
    print(f'{calc.dividir(a, b)}')