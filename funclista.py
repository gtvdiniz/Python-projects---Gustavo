class Encadeada: 
    def __init__(self):
        self.cabeca = None 
        
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
        
class NodoLista: 
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado 
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    



def insereinicio(lista, novodado):
    novo_nodo = NodoLista(novodado)
    
    novo_nodo.proximo = lista.cabeca
    
    lista.cabeca = novo_nodo
    
    
    
def busca(lista, valor):
    corrente = lista.cabeca 
    while corrente and corrente.dado != valor: 
        corrente = corrente.proximo 
    return corrente 


def remove(self, valor):
    assert self.cabeca, "Impossível remover valor de lista vazia."
    if self.cabeca.dado == valor: 
        self.cabeca = self.cabeca.proximo 
        
    else: 
        anterior = None 
        corrente = self.cabeca 
        while corrente and corrente.dado != valor: 
            anterior = corrente 
            corrente = corrente.proximo  
            
        if corrente:
            anterior.proximo = corrente.proximo 
        else: 
            anterior.proximo = None 


lista = Encadeada()
print("Lista vazia", lista)

insereinicio(lista, 10)
insereinicio(lista, 10)
insereinicio(lista, 7)
insereinicio(lista, 5)
insereinicio(lista, 1)
insereinicio(lista, 1)
insereinicio(lista, 0)

print("Lista após inserções:", lista)

for i in range(10, 9, -2): 
    elemento = busca(lista, i)
    if elemento: 
        print("Elemento {0} presente na lista".format(i))

    else: 
         print("Elemento {0} não encontrado".format(i)) ###Exemplo de Busca


for i in range(11):
    remove(lista, i)
print("Removendo o elemento {0}: {1}".format(i, lista)) ###Exemplo de remoção