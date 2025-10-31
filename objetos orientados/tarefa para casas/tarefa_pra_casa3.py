
class Produto:
    def __init__(self, nome, quantidade, valor_unitario):
        if valor_unitario <= 0:
            raise ValueError("Valor unitário deve ser positivo.")
        self.nome = nome
        self._quantidade = quantidade
        self.__valor_unitario = valor_unitario

    def vender(self, qtd):
        if qtd > self._quantidade:
            print(f"Estoque insuficiente para {self.nome}.")
        else:
            self._quantidade -= qtd
            print(f"Venda: {qtd} x R$ {self.__valor_unitario:.2f} = R$ {qtd * self.__valor_unitario:.2f}")

    def report_estoque(self, qtd):
        self._quantidade += qtd

    def mostrar_quantidade(self):
        print(f"{self.nome}: {self._quantidade} unidades")

    def mostrar_valor_total(self):
        print(f"{self.nome}: R$ {self._quantidade * self.__valor_unitario:.2f}")
        
caneta = Produto("Caneta", 100, 2.50)
caderno = Produto("Caderno", 50, 15.00)

caneta.vender(20)
caneta.report_estoque(50)

caneta.mostrar_quantidade()
caderno.mostrar_quantidade()

caneta.mostrar_valor_total()
caderno.mostrar_valor_total()