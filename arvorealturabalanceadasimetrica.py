#4. Calcule a altura de uma BST.
#5. Verifique se uma árvore binária é balanceada.
#6. Determine se uma árvore é simétrica

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave,
                                   self.direita and self.direita.chave)

    def em_ordem(self, raiz):
        if not raiz:
            return

        self.em_ordem(raiz.esquerda)
        print(raiz.chave),
        self.em_ordem(raiz.direita)

    def insere(self, raiz, nodo):
        """ Insere um nodo em uma árvore binária de pesquisa"""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            raiz = nodo


        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)

        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)

    def busca(self, raiz, chave):
        """Procura por uma chave em uma árvore binária de pesquisa"""


        if raiz is None:
            return None

        if raiz.chave == chave:
            return raiz

        if raiz.chave < chave:
            return self.busca(raiz.direita, chave)

        return self.busca(raiz.esquerda, chave)


    def altura(self, raiz):
        """Verifica a altura da árvore binária """
        if raiz is None:
            return -1
        else:
            altura_esquerda = self.altura(raiz.esquerda)
            altura_direita = self.altura(raiz.direita)
            return 1 + max(altura_esquerda, altura_direita)


    def balanceada(self, raiz):
        """Verifica se a árvore binária está balanceada"""
        if raiz is None:
            return True
        altura_esquerda = self.altura(raiz.esquerda)
        altura_direita = self.altura(raiz.direita)

        if abs(altura_esquerda - altura_direita) > 1:
            return False
        return self.balanceada(raiz.esquerda) and self.balanceada(raiz.direita)


    def simetrica(self,raiz):
        """Verifica se a árvore binária é simétrica"""
        if raiz is None:
            return True
        altura_esquerda = self.altura(raiz.esquerda)
        altura_direita = self.altura(raiz.direita)

        if abs(altura_esquerda) != abs(altura_direita):
            return False
        return self.simetrica(raiz.esquerda) and self.simetrica(raiz.direita)

###############################################
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz.insere(raiz, nodo)

altura = raiz.altura(raiz)
print(f"Árvore com altura total: {altura}")

if raiz.balanceada(raiz):
    print("Árvore é balanceada")
else:
    print("Árvore não é balanceada")

if raiz.simetrica(raiz):
    print("Árvore simétrica\n\n")
else:
    print("Árvore não é simétrica\n\n")
###############################################
raiz2 = NodoArvore()
for chave2 in []:
    nodo2 = NodoArvore(chave2)
    raiz2.insere(raiz2, nodo2)
altura2 = raiz2.altura(raiz2)
print(f"Árvore com altura total: {altura2}")

if raiz2.balanceada(raiz2):
    print("Árvore é balanceada")
else:
    print("Árvore não é balanceada")

if raiz2.simetrica(raiz2):
    print("Árvore simétrica\n\n")
else:
    print("Árvore não é simétrica\n\n")
###############################################
raiz3 = NodoArvore(60)
for chave3 in [70,80,90,100,110,107,5,4,3,2,7,9,0,1]:
    nodo3 = NodoArvore(chave3)
    raiz3.insere(raiz3, nodo3)
altura3 = raiz3.altura(raiz3)
print(f"Árvore com altura total: {altura3}")

if raiz3.balanceada(raiz3):
    print("Árvore é balanceada")
else:
    print("Árvore não é balanceada")

if raiz3.simetrica(raiz3):
    print("Árvore simétrica\n\n")
else:
    print("Árvore não é simétrica\n\n")




