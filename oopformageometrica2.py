import math

class FormaGeometrica:
    def __init__(self, cor):
        self.cor = cor

    def imprimir_numero_lados(self):
        pass

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado, cor):
        super().__init__(cor)
        self.lado = lado

    def imprimir_numero_lados(self):
        return f"Quadrado: 4 lados"

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, cor):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def imprimir_numero_lados(self):
        return f"Triângulo: 3 lados"

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
       
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio, cor):
        super().__init__(cor)
        self.raio = raio

    def imprimir_numero_lados(self):
        return f"Círculo: infinitos lados"

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
      
        pass


quadrado = Quadrado(lado=5, cor="verde")
print(quadrado.imprimir_numero_lados())
print(f"Área do quadrado: {quadrado.calcular_area()}")

triangulo = Triangulo(base=6, altura=4, cor="azul")
print(triangulo.imprimir_numero_lados())
print(f"Área do triângulo: {triangulo.calcular_area()}")

circulo = Circulo(raio=3, cor="vermelho")
print(circulo.imprimir_numero_lados())
print(f"Área do círculo: {circulo.calcular_area()}")
