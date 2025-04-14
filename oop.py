class Carros:
    def __init__(self, fab, model, ano ):
        self.fabricante = fab
        self.modelo = model 
        self.ano = ano 
    def showCarro(self):
        print(f'Fabricante: {self.fabricante} "\n" Modelo: {self.modelo} "\n" Ano:{self.ano}')





#main
carro1 = Carros('Honda', 'Fit', 2020)
carro2 = Carros('Fiat', 'Uno', 2010)
carro3 = Carros('GM', 'Zafira', 2015)

print(f'fabricante: {carro1.fabricante} modelo: {carro1.modelo} ano:{carro1.ano}')
print(f'fabricante: {carro2.fabricante} modelo: {carro2.modelo} ano:{carro2.ano}')
print(f'fabricante: {carro3.fabricante} modelo: {carro3.modelo} ano:{carro3.ano}')


carro1.showCarro()

carro2.showCarro()

carro3.showCarro()