class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.lista_produtos = []

    def adicionar(self, produto):
        self.lista_produtos.append(produto)

    def calcular_total(self):
        return sum(p.preco for p in self.lista_produtos)

p1 = Produto("Camisa", 50)
p2 = Produto("Calça", 80)
p3 = Produto("Tênis", 120)



carrinho = CarrinhoDeCompras()
carrinho.adicionar(p1)
carrinho.adicionar(p2)
carrinho.adicionar(p3)

print(f"Total da compra: R${carrinho.calcular_total():.2f}")



class Passageiro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Onibus:
    def __init__(self, linha, capacidade):
        self.linha = linha
        self.capacidade = capacidade
        self.lista_passageiros = []

    def embarcar(self, passageiro):
        if len(self.lista_passageiros) < self.capacidade:
            self.lista_passageiros.append(passageiro)
        else:
            print(f"Capacidade máxima de {self.capacidade} passageiros.")

    def listar_passageiros(self):
        for p in self.lista_passageiros:
            print(f"{p.nome}, {p.idade} anos")

onibus = Onibus("Linha 123", 2)
p1 = Passageiro("Hayssa", 30)
p2 = Passageiro("Sabrina", 25)
p3 = Passageiro("Ruane", 40)


onibus.embarcar(p1)
onibus.embarcar(p2)
onibus.embarcar(p3) 


print("Passageiros embarcados:")
onibus.listar_passageiros()

