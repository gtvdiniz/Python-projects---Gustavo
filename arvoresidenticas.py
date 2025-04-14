#3. Verifique se duas árvores binárias são idênticas.

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


    def identicas_s(self, raiz1, raiz2):
        if raiz1 is None and raiz2 is None:
            return True

        elif raiz1 is not None and raiz2 is not None:
            if (raiz1.chave == raiz2.chave and
                    self.identicas_s(raiz1.esquerda, raiz2.esquerda) and
                    self.identicas_s(raiz1.direita,raiz2.direita)):
                return True


        return False

raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz.insere(raiz, nodo)

#Árvore Igual
raiz2 = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz2.insere(raiz2, nodo)

#Árvore Diferente
raiz3 = NodoArvore(41)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz3.insere(raiz3, nodo)

if raiz.identicas_s(raiz, raiz2):
    print("As árvores são identicas!")

else:
    print("As árvores são diferentes!\n")


if raiz.identicas_s(raiz, raiz3):
    print("As árvores são identicas!")

else:
    print("As árvores são diferentes!")

