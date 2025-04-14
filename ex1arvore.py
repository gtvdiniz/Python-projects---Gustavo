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

    def menor_elemento(self, raiz):
        """ Encontra o menor elemento de uma árvore binária de pesquisa"""
        atual = raiz
        while atual and atual.esquerda:
            atual = atual.esquerda
        return atual

# Exemplo de uso
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    raiz.insere(raiz, nodo)

# Encontrando o menor elemento
menor_nodo = raiz.menor_elemento(raiz)
if menor_nodo:
    print(f'O menor elemento é: {menor_nodo.chave}')



resultado = raiz.busca(raiz,chave)

