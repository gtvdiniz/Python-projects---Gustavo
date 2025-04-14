class Veiculo:
    def __init__(self, capacidade, quantidade_rodas):
        self.capacidade = capacidade
        self.quantidade_rodas = quantidade_rodas
        self.velocidade = 0

    def acelerar(self):
        pass  

    def frear(self):
        pass 

    def mostrar_painel(self):
        print(f"Velocidade atual: {self.velocidade} Km/h")

class Automovel(Veiculo):
    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10

class Bicicleta(Veiculo):
    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 1:
            self.velocidade -= 1

automovel = Automovel(capacidade=4, quantidade_rodas=4)
bicicleta = Bicicleta(capacidade=1, quantidade_rodas=2)

automovel.acelerar()
automovel.mostrar_painel()
automovel.frear()
automovel.mostrar_painel()

bicicleta.acelerar()
bicicleta.mostrar_painel()
bicicleta.frear()
bicicleta.mostrar_painel()
