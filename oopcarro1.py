class Carro: 
    def __init__(self, model, ano, vel):
        self.modelo = model 
        self.ano = ano
        self.velocidade = vel
    def showCarro(self):
        print(f'\n Modelo: {self.modelo} \n Ano: {self.ano} \n Velocidade Máxima:{self.velocidade} \n')




carro1=Carro('Bugatti Chiron','2022','310km/h')
carro2=Carro('Ferrari Purosangue','2016','420 km/h')
carro3=Carro('Lamborghini Sian FKP 37','2019','347km/h')






carro1.showCarro()
carro2.showCarro()
carro3.showCarro()