class COPO:
    def __init__(self, capacidade):
        if capacidade not in [250, 300, 500]:
            raise ValueError("Capacidade inválida. Escolha entre 250, 300 ou 500 ml.")
        self.capacidade = capacidade
        self.conteudo = 0

    def Fill(self, x):
        if self.conteudo + x > self.capacidade:
            raise ValueError("Excedendo a capacidade máxima do copo.")
        self.conteudo += x

    def Empty(self):
        self.conteudo = 0

    def Status(self):
        return f"O copo contém {self.conteudo} ml de {self.capacidade} ml disponíveis."

# Testando a classe
copo = COPO(300)
copo.Fill(150)
print(copo.Status())  # Deve imprimir: O copo contém 150 ml de 300 ml disponíveis.
copo.Fill(100)
print(copo.Status())  # Deve imprimir: O copo contém 250 ml de 300 ml disponíveis.
copo.Empty()
print(copo.Status())  # Deve imprimir: O copo contém 0 ml de 300 ml disponíveis.
