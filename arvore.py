class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita



    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave,
                                     self.direita and self.direita.chave)

    def insere(self, raiz, nodo):
        """ Insere um nodo em uma árvore binária de pesquisa"""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            raiz = nodo

        # Nodo deve ser inserido na subárvore direita.
        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
               raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)


        #Nodo deve ser inserido na subárvore esquerda.
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)




    def busca(self,raiz, chave):
        """Procura por uma chave em uma árvore binária de pesquisa"""

        #Trata o caso em que uma chave procurada não está presente.
        if raiz is None:
            return None

        #A chave procurada está na raiz da árvore
        if raiz.chave == chave:
            return raiz


        #A chave procurada é maior que a raiz
        if raiz.chave < chave:
            return self.busca(raiz.direita, chave)


        #A chave procurada é menor que a raiz
        return self.busca(raiz.esquerda, chave)




# Cria uma árvore binária de pesquisa
raiz = NodoArvore(40)

for chave in [-50, 10, 30, 70, 100]:
    nodo = NodoArvore(chave)
    raiz.insere(raiz, nodo)

    print(raiz)
