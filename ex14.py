class Funcionario: 
    def __init__(self):
        self.nome = input("Escreva o nome do funcionário: ")
        self.salario = float(input("Digite aqui seu salário: "))
        
    def showInformações(self):
        print(f'\nNome:{self.nome}          Salário: {self.salario}\n')
        
        
    def aumentoSalarial(self): 
        if self.salario <= 1500: 
            novosalario = self.salario + self.salario * 0.25
            print(f'\nAumento de 25%            Novo Salário: {novosalario}')
            
        elif self.salario <= 2500:
            novosalario = self.salario + self.salario * 0.20
            print(f'\nAumento de 20%            Novo Salário: {novosalario}')
        
        elif self.salario <= 5000:
            novosalario = self.salario + self.salario * 0.15
            print(f'\nAumento de 15%            Novo Salário: {novosalario}')
            
        elif self.salario <= 7000: 
            novosalario = self.salario + self.salario * 0.10
            print(f'\nAumento de 10%            Novo Salário: {novosalario}')
            
        elif self.salario > 7000:
            novosalario = self.salario + self.salario * 0.05
            print(f'\nAumento de 5%            Novo Salário: {novosalario}')
        
a = Funcionario()
a.showInformações()
a.aumentoSalarial()