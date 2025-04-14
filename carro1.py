class Automovel:


    def __init__(self, placa='XX-123'):
        self.placa = placa 
        
    def get_placa(self):
        return self.placa
    
    def dirigir(self, velocidade):
        print('Estou dirigindo a %d \ km/h' % velocidade)
        
        
        
   