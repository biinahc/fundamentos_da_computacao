class Transporte:
    def mover(self): pass

class Carro(Transporte):
    def mover(self): return "O carro está se movendo 🚗"

class Bicicleta(Transporte):
    def mover(self): return "A bicicleta está pedalando 🚴"

class Aviao(Transporte):
    def mover(self): return "O avião está voando ✈️"

class Barco(Transporte):
    def mover(self): return "O barco está navegando 🚢"

transportes = [Carro(), Bicicleta(), Aviao(), Barco()]
for t in transportes:
    
    print(t.mover())