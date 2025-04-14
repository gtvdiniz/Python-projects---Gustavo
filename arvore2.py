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

        # Nodo deve ser inserido na subárvore direita.
        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)


        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)

    def busca(self, raiz, chave):
        """Procura por uma chave em uma árvore binária de pesquisa"""

        # Trata o caso em que uma chave procurada não está presente.
        if raiz is None:
            return None

        # A chave procurada está na raiz da árvore
        if raiz.chave == chave:
            return raiz

        # A chave procurada é maior que a raiz
        if raiz.chave < chave:
            return self.busca(raiz.direita, chave)

        # A chave procurada é menor que a raiz
        return self.busca(raiz.esquerda, chave)


    def identico(self, raiz1, raiz2):
        """Compara árvores binárias para ver se são iguais"""
        if raiz1 is None and raiz2 is None:
            return True

        elif raiz1 is not None and raiz2 is not None:
            if (raiz1.chave == raiz2.chave and self.identico(raiz1.esquerda,raiz2.esquerda) and
             self.identico(raiz1.direita, raiz2.direita)):
                return True



        return False


# Criando a árvore
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz.insere(raiz, nodo)
# Chamando o método em_ordem no objeto raiz
raiz.em_ordem(raiz)
print("\n")

raiz2 = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz2.insere(raiz2, nodo)
# Chamando o método em_ordem no objeto raiz
raiz2.em_ordem(raiz2)
print("\n")


if raiz.identico(raiz, raiz2):
    print("As árvores são iguais!")

else:
    print("As árvores não são iguais")


