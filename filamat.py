class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado=None, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada"""
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""
        novo_nodo = Nodo(novo_dado)
        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self):
        """Remove o primeiro elemento da fila e retorna seu dado."""
        assert self.primeiro is not None, "Impossível remover elemento de fila vazia."
        dado = self.primeiro.dado
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        return dado

    def esta_vazia(self):
        return self.primeiro is None


def avaliar_expressao(expressao):
    """Avalia uma expressão matemática com suporte para parênteses, colchetes e chaves"""
    fila_operadores = Fila()
    fila_operandos = Fila()

    # Definindo a precedência dos operadores
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    operadores = []
    operandos = []

    def aplicar_operacao():
        """Aplica a operação no topo da pilha de operadores aos dois operandos no topo da pilha de operandos"""
        operador = operadores.pop()
        operando2 = operandos.pop()
        operando1 = operandos.pop()
        if operador == '+':
            resultado = operando1 + operando2
        elif operador == '-':
            resultado = operando1 - operando2
        elif operador == '*':
            resultado = operando1 * operando2
        elif operador == '/':
            resultado = operando1 / operando2
        operandos.append(resultado)

    for char in expressao:
        if char.isdigit():
            operandos.append(int(char))
        elif char in precedencia:
            while (operadores and operadores[-1] in precedencia and
                   precedencia[operadores[-1]] >= precedencia[char]):
                aplicar_operacao()
            operadores.append(char)
        elif char in '([{':
            operadores.append(char)
        elif char in ')]}':
            while operadores and operadores[-1] not in '([{':
                aplicar_operacao()
            operadores.pop()  # Remove o parêntese correspondente

    while operadores:
        aplicar_operacao()

    return operandos[0]

# Programa Principal
expressao = input("Digite uma expressão matemática (ex: 3+2*(2+1)): ")
resultado = avaliar_expressao(expressao)
print(f"Resultado da expressão '{expressao}' é: {resultado}")
