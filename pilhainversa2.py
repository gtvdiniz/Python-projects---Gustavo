class Nodo: 
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado 
        self.anterior = nodo_anterior
       
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
    
class Pilha: 
    """Esta classe representa uma pilha encadeada"""
    
    def __init__(self):
        self.topo = None 
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"
        
    # Inserindo elemento 
    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo 
        self.topo = novo_nodo

    # Inverter a pilha
    def inverter(self):
        elementos = []
        atual = self.topo
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.anterior
        
        self.topo = None  # Esvazia a pilha original
        
        for dado in elementos:
            self.inserir(dado)

pilha = Pilha()
print("Pilha vazia:", pilha)   

for i in range(5):
    num = int(input("Digite um número: "))
    pilha.inserir(num)
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha))

print("Pilha antes de inverter:")
print(pilha)

pilha.inverter()

print("Pilha invertida:")
print(pilha)



