class Produto:

    def __init__(self, nome, quantidade, valor_unitario):
        self.nome = nome
        self._quantidade = quantidade
        if valor_unitario <= 0:
            raise ValueError("Valor invalido")
        self.__valor_unitario = valor_unitario

    def vender(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida.")
            return
        if quantidade > self._quantidade:
            print(f"Estoque baixo para vender {quantidade} unidades de {self.nome}.")
        else:
            self._quantidade -= quantidade
            valor_venda = quantidade * self.__valor_unitario
            print(f"Venda realizada: {quantidade} unidades de {self.nome} por R$ {valor_venda:.2f}")

    def report_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida para reposição.")
            return
        self._quantidade += quantidade
        print(f"Estoque atualizado: {self.nome} agora tem {self._quantidade} unidades.")

    def mostrar_quantidade(self):
        print(f"{self.nome}: {self._quantidade} unidades em estoque.")

    def mostrar_valor_total(self):
        print(f"Valor total em estoque de {self.nome}: R$ {self.__valor_total():.2f}")

    def __valor_total(self):
        return self._quantidade * self.__valor_unitario
