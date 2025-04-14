class BombadeCombustivel:
    def __init__(self, combus, grana, qtdc):
       self.combus = combus 
       self.grana = grana  
       self.qtdc = qtdc
       self.gasolina = 6.13
       self.etanol = 4.08
    
    def tipoCombustivel(self):
        while True: 
            comb = int(input("Escolha o tipo de combustível:\n[1] - Etanol\n[2] - Gasolina\n\n:"))
            if comb == 1: 
                self.combus = 'Etanol'
                print(f'Você escolheu {self.combus} como combustível')
                break
            elif comb == 2: 
                self.combus = 'Gasolina'
                print(f'Você escolheu {self.combus} como combustível')
                break
            else: 
                print("Digite um opção correta !!!")
                
    def valorLitro(self):
        if self.combus == 'Gasolina':
            print(f"\nA {self.combus} está {self.gasolina} por litro")
        
        else: 
            print(f'\nO {self.combus} está {self.etanol} por litro')
            
    def quantidadeCombustivel(self):
        qtd = float(input("Informe a quantidade que você possuí em litros de combustível: "))
        self.qtdc = qtd 
        
    def abastecerporValor(self):
        dinheiro = float(input("Digite a quantidade de dinheiro que você possui: "))
        
        if self.combus ==  'Gasolina':
            valorabas = dinheiro / self.gasolina
            print(f"Você conseguirá {valorabas:.2f} de Gasolina")
            
        elif self.combus == 'Etanol':
            valorabas = dinheiro / self.etanol
            print(f"Você conseguirá {valorabas:.2f} de Etanol")
            
    def abastecerporLitro(self):
        litros = float(input("Digite a quantidade de litros que você quer abastecer: "))
        
        if self.combus ==  'Gasolina':
            valorabas = litros* self.gasolina
            print(f"Você terá que pagar {valorabas:.2f}")
            
            
        elif self.combus == 'Etanol':
            valorabas = litros * self.etanol
            print(f"Você terá que pagar {valorabas:.2f}")
            
    def alterarValor(self):
        if self.combus == 'Gasolina':
            new_valor = float(input("Digite um novo valor: "))
            self.gasolina = new_valor
            
        else: 
            new_valor = float(input("Digite um novo valor: "))
            self.etanol = new_valor
            
        
        
    def alterarCobustivel(self):
        troca = int(input("Você quer trocar o combustível?\n[1] - Sim\n[2] - Não\n:"))
        if troca == 1 and self.combus == 'Gasolina':
            self.combus == 'Etanol'
            print(f'Combustível trocado para {self.combus}')
            
        elif troca == 1 and self.combus == 'Etanol':
            self.combus == 'Gasolina'
            print(f'Combustível trocado para {self.combus}')
            
        elif troca == 2: 
            print("Ok!")
            
    def alterarQuantidadeCombustivel(self):
        novaqtd = float(input("Digite sua nova quantidade de combustível: "))
        self.qtdc = novaqtd 
        print(f'Quantidade de combustível alterada para {self.qtdc:.2f}')
        
        
a = BombadeCombustivel('','', '')
a.tipoCombustivel()
a.valorLitro()

while True: 
    op = int(input("\nDigite uma opção:\n[1] - Abastecer por Valor\n[2] - Abastecer por Litro\n[3] - Alterar valor do Litro\n[4] - Alterar combustível\n[5] - Alterar quantidade de combustível\n[6] - Sair\n\n:"))
    
    if op == 1:
        a.abastecerporValor()
        
    elif op == 2:
        a.abastecerporLitro()
    
    elif op == 3: 
        a.alterarValor()
        
    elif op == 4: 
        a.alterarCobustivel()
        
    elif op == 5: 
        a.alterarQuantidadeCombustivel
        
    elif op == 6:
        break