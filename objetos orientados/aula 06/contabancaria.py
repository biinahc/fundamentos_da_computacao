#Implemente duas classes: ContaBancaria e Cliente
#1- Faça com que a ContaBancaria utilize um objeto Cliente(que ja existe no sistema)
#qual relacionamento é esse?
# 2- Se a contaBancaria fosse composta por um objeto ExtratoBancario (que só existe oara aquela conta), como seria a inicialização ? 


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

#ela é agregação
class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente 
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"Conta {self.numero} | Cliente: {self.cliente.nome} | Saldo: R${self.saldo:.2f}"
    
    def __del__ (self):
        print(f"Conta {self.numero} encerrada. ")



cliente1 = Cliente("Sabrina Caldas", "02727542260") #já existe

conta = ContaBancaria("0001", cliente1) #agregacao
conta.depositar(1000)
print(conta)
