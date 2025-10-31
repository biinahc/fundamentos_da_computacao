# Crie um sistema simples de Pedido Online que demonstre tanto a Composição quanto a
# Agregação:
# Crie a classe Produto. (Entidade independente, vida longa).
# Crie a classe ItemPedido. (Entidade dependente, representa um produto dentro de um
# pedido).
# Crie a classe Pedido (o "todo").
# A classe Pedido deve:
# Ter uma relação de Composição com a classe ItemPedido (os itens são criados e morrem
# junto com o pedido).
# Ter uma relação de Agregação com a classe Produto (o pedido usa uma referência ao
# produto, mas não o destrói).
# Implemente o código e demonstre a diferença no ciclo de vida ao criar um Produto, criar um
# Pedido (com o produto), e depois deletar o Pedido.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto  
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.itens = []  

    def adicionar_item(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)

    def total(self):
        return sum(item.produto.preco * item.quantidade for item in self.itens)

produto1 = Produto("Camiseta", 50.0)  
pedido = Pedido()
pedido.adicionar_item(produto1, 2)

print(f"Total do pedido: R${pedido.total():.2f}") 

del pedido  
print(f"Produto ainda existe: {produto1.nome} - R${produto1.preco:.2f}")  