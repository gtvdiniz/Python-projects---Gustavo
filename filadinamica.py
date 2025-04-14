class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada"""
    def __init__(self, dado=0, proximo_nodo=None):
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

    def push(self, novo_dado):
        """Insere um elemento no final da fila."""
        novo_nodo = Nodo(novo_dado)
        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        """Remove o primeiro elemento da fila."""
        assert self.primeiro is not None, "Impossível remover elemento de fila vazia."
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None

    def busca(self, valor):
        """Busca um valor na fila e retorna sua posição (1-indexada)."""
        atual = self.primeiro
        posicao = 1
        while atual is not None:
            if atual.dado == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        return -1  # Retorna -1 se o valor não for encontrado

    def imprime(self):
        """Percorre e imprime todos os elementos da fila."""
        atual = self.primeiro
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()

    def inverte(self):
        """Inverte a ordem dos elementos da fila."""
        anterior = None
        atual = self.primeiro
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.primeiro, self.ultimo = self.ultimo, self.primeiro


# Testando todas as funcionalidades

# Cria uma fila vazia            
fila = Fila()
print("Fila vazia: ", fila)

# Insere elementos na fila.
for i in [1, 4, 5, 2]:
    fila.push(i)
    print("Insere o valor {0} na fila: {1}".format(i, fila))

# Busca um valor na fila
valor = 5
posicao = fila.busca(valor)
print("O valor {0} está na posição {1}".format(valor, posicao))

# Imprime todos os elementos da fila
print("Elementos na fila: ", end="")
fila.imprime()

# Inverte a ordem dos elementos da fila
fila.inverte()
print("Fila invertida: ", end="")
fila.imprime()

# Remove elementos da fila
while fila.primeiro is not None:
    fila.pop()
    print("Removendo elemento: ", fila)
