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
    contagem = 0
    while corrente:
        if corrente.dado == valor:
            contagem += 1
        corrente = corrente.proximo
    return contagem


def remove(lista, valor):
    corrente = lista.cabeca
    anterior = None
    encontrado = False
    while corrente: 
        if corrente.dado == valor:
            if encontrado:
                if anterior:
                    anterior.proximo = corrente.proximo
                else:
                    lista.cabeca = corrente.proximo
            else:
                encontrado = True
                anterior = corrente
        else:
            anterior = corrente
        corrente = corrente.proximo

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


contagem_10 = busca(lista, 10)
print("Número de elementos iguais a 10:", contagem_10)

contagem_7 = busca(lista, 7)
print("Número de elementos iguais a 7:", contagem_7)

contagem_5 = busca(lista, 5)
print("Número de elementos iguais a 5:", contagem_5)

contagem_1 = busca(lista, 1)
print("Número de elementos iguais a 1:", contagem_1)

contagem_0 = busca(lista, 0)
print("Número de elementos iguais a 0:", contagem_0)



remove(lista, 10)
remove(lista, 7)
remove(lista, 5)
remove(lista, 1)
remove(lista, 0)
print("Lista após remoção de duplicatas:", lista)
