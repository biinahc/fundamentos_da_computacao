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