class Calculadora:
    def __init__(self):
        self.num1 = float(input("Número: "))
        self.num2 = float(input("Número: "))

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Erro: Divisão por zero não é permitida"

calc = Calculadora()

print(f'Soma: {calc.soma()}')
print(f'Subtração: {calc.subtracao()}')
print(f'Multiplicação: {calc.multiplicacao()}')
print(f'Divisão: {calc.divisao()}')
