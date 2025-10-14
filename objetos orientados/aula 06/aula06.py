class motor:
    """A 'parte que é essencial e dependente'"""
    def __init__(self, tipo):
        self.tipo = tipo
        self.ligado = False
        print (f" -> motor {self.tipo} foi montado.")


    def ligar (self):
        self.ligado = True
        print (f" -> motor {self.tipo} ligado. vrummmmmmmm")


    def ___del___ (self):
        """O motor é destruido quando o objeto Carro é apagado"""
        print (f" -> motor {self.tipo}foi desmontado/destruido")

class Carro:
    """O 'todo' que contém e controla o Motor'"""
    def __init__(self, modelo, tipo_motor):
        self.modelo = modelo
        self.motor = motor(tipo_motor)
        print (f" Carro {self.modelo} saiu da fabrica")

    def dirigir (self):
        if not self.motor.ligar:
            self.motor.ligar()
        print (f" Carro {self.modelo} esta em movimento")


    def ___del___ (self):
        """Quando o carro é destruido, ele leva o Motor com ele."""
        print (f" Carro '{self.modelo}'foi para o ferro-velho/sucateado")

    
print ("1. Criando um novo carro (e seu motor).")
meu_carro = Carro("FUSCA", "1.5L")

print("\n2. Usando o carro:")

meu_carro.dirigir()

print("\n. Sucateando o carro (fim do ciclo de vida):")

del meu_carro

print("\nFim da simulação")