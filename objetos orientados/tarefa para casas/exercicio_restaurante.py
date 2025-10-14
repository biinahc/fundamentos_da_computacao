class Restaurante:
    def __init__(self, nome):
        self.__nome = nome
        self.__cardapio = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if novo_nome: self.__nome = novo_nome

    def adicionar_prato(self, prato):
        if prato not in self.__cardapio: self.__cardapio.append(prato)

    def listar_cardapio(self):
        print("Cardápio:", ", ".join(self.__cardapio))

    def atender_cliente(self, cliente, prato):
        msg = f"{cliente}, seu pedido de {prato} foi confirmado." if prato in self.__cardapio else f"{cliente}, o prato {prato} não está disponível."
        print(msg)

r = Restaurante("Sabor Caseiro")
for p in ["Feijoada", "Lasanha", "Salada"]: r.adicionar_prato(p)
r.atender_cliente("Ana", "Feijoada")
r.atender_cliente("João", "Pizza")
r.set_nome("Sabor da Vó")
print("Novo nome:", r.get_nome())
r.listar_cardapio()