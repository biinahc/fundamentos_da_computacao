class Operacao:
    def calcular(self, a, b):
        pass

class Soma(Operacao):
    def calcular(self, a, b):
        return a + b

class Subtracao(Operacao):
    def calcular(self, a, b):
        return a - b

class Multiplicacao(Operacao):
    def calcular(self, a, b):
        return a * b

class Divisao(Operacao):
    def calcular(self, a, b):
        return a / b if b != 0 else "Erro"

ops = [Soma(), Subtracao(), Multiplicacao(), Divisao()]

for op in ops:
    print(f"{op.__class__.__name__}: {op.calcular(10, 5)}")
    
    