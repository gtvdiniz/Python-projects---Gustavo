class Retangulo:
    def __init__(self,l, a):
       self.largura = l 
       self.altura = a

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2*(self.largura + self.altura)
    

    #main
ret1 = Retangulo(10, 5)
ret2 = Retangulo(7, 4)

print(f'Area do retangulo 1: {ret1.area()} \n Perimetro: {ret1.perimetro()}')
print(f'\n Area do retangulo 1: {ret1.area()} \n Perimetro: {ret1.perimetro()}')


       