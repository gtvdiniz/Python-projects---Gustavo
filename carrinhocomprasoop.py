class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, preco, quantidade):
        if nome not in self.itens:
            self.itens[nome] = {'preco': preco, 'quantidade': quantidade}
        else:
            self.itens[nome]['quantidade'] += quantidade

    def remover_item(self, nome, quantidade):
        if nome in self.itens:
            if quantidade >= self.itens[nome]['quantidade']:
                del self.itens[nome]
            else:
                self.itens[nome]['quantidade'] -= quantidade

    def total(self):
        return sum(item['preco'] * item['quantidade'] for item in self.itens.values())

# Cria uma instância da classe CarrinhoDeCompras
carrinho = CarrinhoDeCompras()

# Adiciona alguns itens
carrinho.adicionar_item('maçã', 1.00, 5)
carrinho.adicionar_item('banana', 0.50, 10)

# Remove alguns itens
carrinho.remover_item('maçã', 2)

# Calcula o total
print(f'Total: {carrinho.total()}')
