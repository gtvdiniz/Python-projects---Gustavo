class ContaCorrente: 
        def __init__(self):
            self.nconta = input("Informe o número da conta: ")
            self.nome = input("Informe o nome do correntista: ")
            self.saldo = float(input("Informe o saldo da conta: "))
    
    
        def AlterarNome(self):
            novonome = input("Informe o novo nome do correntista: ")
            self.nome = novonome
        
        def depositar(self):
            deposito = float(input("Digite o valor do depósito: "))
            self.saldo = deposito + self.saldo
            
            print(f'O valor depositado foi de {deposito} Reais')
            
            
            
        def saque(self):
            saque = float(input("Digite o valor a sacar: "))
            if saque > self.saldo: 
                print("Erro !!!!!!!!!")             #O valor a ser sacado não pode ser maior que o valor que está no saldo. 
            else: 
                self.saldo = self.saldo - saque 
            
            print(f'O valor sacado foi de {saque} Reais')
            
        def showConta(self):
            print(f'Número da conta: {self.nconta}\nNome do Correntista: {self.nome}\nSaldo da Conta: {self.saldo}')
            
            
a  = ContaCorrente()

while True: 
    op = int(input("Escolha uma das opções:\n[1] - Alterar Nome da Conta\n[2] - Depositar dinheiro\n[3] - Sacar dinheiro\n[4] - Mostrar Detalhes da Conta\n[5] - Sair\n:"))
    
    if op == 1: 
        a.AlterarNome()
       
        
    elif op == 2: 
        a.depositar()
        
        
    elif op == 3: 
        a.saque()
        
    elif op == 4: 
        a.showConta()
       
        
    elif op == 5:
        break
    
    else: 
        print("Digite uma opção correta!")