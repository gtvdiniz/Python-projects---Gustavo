class Pessoa: 
    def __init__(self, nome, sexo, cpf):
        self.nome = nome 
        self.sexo = sexo 
        self.cpf = cpf 
    
    def showPessoa(self):
        print(f'\nNome:{self.nome}, Sexo:{self.sexo}, CPF:{self.cpf}\n')
    

p1 = Pessoa('Augusto', 'Masculino', 16321321421)

p2 = Pessoa('Jorge', 'Masculino', 205215125215)

p3 = Pessoa('Ana', 'Feminino', 5162412421421)


p1.showPessoa()

p2.showPessoa()

p3.showPessoa()