class Pneu:
    def __init__(self, marca):
        self.marca = marca
        print (f" -> Pneu {self.marca} fabricado.")


    def ___del___ (self):        
        print (f" Pneu {self.marca}descartado da memoria")


class Carro:
    def __init__(self, modelo, pneu_reserva):
        self.modelo = modelo
        self.pneu_reserva = pneu_reserva
        print (f" Carro {self.modelo}saiu da concessionaria")

    def mostrar_pneu_reserva(self):
        print (f" Carro {self.modelo}é da marca {self.pneu_reserva.marca}.")

    def ___del___ (self):        
        print (f" Carro '{self.modelo}' foi para o ferro-velho")

print ("1. Criando o Pneu (INDIVIDUALMENTE)")
pneu_goodyear = Pneu("Goodyear")

print("\n2.Criando o Carro e AGREGANDO o Pneu: ")

meu_carro= Carro ("Sedan", pneu_goodyear)

print("\n3. Usando o carro:")
meu_carro.mostrar_pneu_reserva()


print("\n4.Destruindo o carro (fim do ciclo de vida do Carro):")

del meu_carro


print("\n.5  O pneu ainda existe (a variavel 'pneu_goodyear' ainda o referencia):")
print("\n. O pneu descartado ? Nao. Marca atual da variavel: {pneu_goodyear.marca} ")

print("\n.6 Destruindo a última referência do Pneu: ")

del pneu_goodyear
