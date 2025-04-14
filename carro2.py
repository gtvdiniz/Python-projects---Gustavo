class Carro: 
    def __init__(self):
        self._nrodas = 4 
    def set_nrodas(self, n): 
        self._nrodas = n 
    def showrodas(self):
        print(self._nrodas)
    
gol = Carro()
gol._nrodas
gol.showrodas()


gol.set_nrodas(10)
gol._nrodas
gol.showrodas()

gol.set_nrodas(6)
gol.showrodas()


