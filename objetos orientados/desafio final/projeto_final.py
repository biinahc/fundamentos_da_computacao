from abc import ABC, abstractmethod
import random

class Equipamento:
    def __init__(self, id, nome, tipo, status):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.__status = None
        self.set_status(status)
        self.sensores = []  

    def ligar(self): self.set_status("ativo")
    def desligar(self): self.set_status("inativo")

    def exibir_status(self):
        print(f"{self.nome} - Status: {self.__status}")

    def get_status(self): return self.__status
    def set_status(self, status):
        if status in ["ativo", "inativo", "em manutenção"]:
            self.__status = status
        else:
            print(f"Status inválido: {status}")

    def adicionar_sensor(self, sensor): self.sensores.append(sensor)

class RoboIndustrial(Equipamento):
    def __init__(self, id, nome, tipo, status, capacidade_operacao):
        super().__init__(id, nome, tipo, status)
        self.capacidade_operacao = capacidade_operacao

    def exibir_status(self):
        super().exibir_status()
        print(f"  Capacidade: {self.capacidade_operacao}")

class EsteiraTransporte(Equipamento):
    def __init__(self, id, nome, tipo, status, velocidade):
        super().__init__(id, nome, tipo, status)
        self.velocidade = velocidade

    def exibir_status(self):
        super().exibir_status()
        print(f"  Velocidade: {self.velocidade} m/s")

class SetorFabrica:
    def __init__(self, nome):
        self.nome = nome
        self.equipamentos = []

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def listar_equipamentos(self):
        for eq in self.equipamentos:
            eq.exibir_status()

class PainelControle:
    def __init__(self, setor):
        self.setor = setor  
    def exibir_informacoes(self):
        print(f"Setor: {self.setor.nome}")
        for eq in self.setor.equipamentos:
            eq.exibir_status()
            for sensor in eq.sensores:
                print(f"  Sensor {sensor.nome}: {sensor.ler_dados()}")

class Sensor(ABC):
    def __init__(self, nome): self.nome = nome
    @abstractmethod
    def ler_dados(self): pass
    def calibrar(self): print("Sensor calibrado com sucesso.")

class SensorTemperatura(Sensor):
    def ler_dados(self): return f"{random.uniform(20, 100):.2f} °C"

class SensorVibracao(Sensor):
    def ler_dados(self): return f"{random.uniform(0.1, 5.0):.2f} m/s²"

eq_simples1 = Equipamento(3, "Ventilador", "Auxiliar", "ativo")
eq_simples2 = Equipamento(4, "Compressor", "Potência", "em manutenção")

eq_simples1.desligar()
eq_simples2.ligar()
eq_simples1.exibir_status() 
eq_simples2.exibir_status()


r1 = RoboIndustrial(1, "Robo A", "Robô", "ativo", "soldagem")
e1 = EsteiraTransporte(2, "Esteira B", "Esteira", "inativo", 1.5)

r1.set_status("voando") 

r1.adicionar_sensor(SensorTemperatura("Temp R1"))
r1.adicionar_sensor(SensorVibracao("Vib R1"))
e1.adicionar_sensor(SensorTemperatura("Temp E1"))

setor1 = SetorFabrica("Montagem")
setor1.adicionar_equipamento(r1)
setor1.adicionar_equipamento(e1)

painel = PainelControle(setor1)
painel.exibir_informacoes()

sensores = [SensorTemperatura("T1"), SensorVibracao("V1")]
for s in sensores:
    print(f"{s.nome}: {s.ler_dados()}")

pilha_manutencao = []
fila_execucao = []

pilha_manutencao.append(r1)
fila_execucao.append(e1)

print("\n--- Pilha de Manutenção ---")
while pilha_manutencao:
    eq = pilha_manutencao.pop()
    print(f"Manutenção: {eq.nome}")

print("\n--- Fila de Execução ---")
while fila_execucao:
    eq = fila_execucao.pop(0)
    eq.ligar()
    eq.exibir_status()
    
    
