import math 
class Circulo:
    def __init__(self):
        self.raioC = float(input("Raio: "))
    
    #Calculo do perimetro
    def perimetro(self):
        return 2 * math.pi * self.raioC

    #Calculo da área
    def area(self):
        return math.pi * (self.raioC ** 2)

# Cria uma instância da classe Circulo
raioC = Circulo()

# Saída dizendo a área e o perímetro
print(f'A área do círculo é: {raioC.area():.2f} \n O perímetro é: {raioC.perimetro():.2f}')
