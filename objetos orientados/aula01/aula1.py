# class Carro:
#     def __init__(self,tipo:str, estado:str, placa:str, numero_de_portas:int ):
#         self.tipo = tipo
#         self.cor = cor 
#         self.placa = placa
#         self.numero_de_portas = numero_de_portas
        


#     def ligar(self):
#         print("f{self.tipo} ligado.")
        
#     def acelerar(self):
#         print("f{self.tipo} está acelerando!")
        
#     def frear(self):
#         print("f{self.tipo} está freiando!")
        
        
# meu_carro = Carro(tipo="Ferrari", cor="Vermelho", placa="JKL-0001", numero_de_portas=4)
# meu_carro.ligar()
# meu_carro.acelerar()
# meu_carro.frear()


#atividade1
#escolha um objeto a sua volta e cite alguns de seus atributo e comportamentos

# class Arcondicionado:
#     def __init__(self, cor: str, potencia: int, temperatura: float, modo: str, estado: str):
#         self.cor = cor
#         self.potencia = potencia
#         self.temperatura = temperatura
#         self.modo = modo
#         self.estado = estado

#     def ligar(self):
#         print(f"O estado do seu ar é: {self.estado}.")

#     def modo_ar(self):
#         print(f"Modo {self.modo} Ativado.")

#     def mostrar_temperatura(self):
#         print(f"{self.temperatura} graus.")

#     def mostrar_potencia(self):
#         print(f"{self.potencia} BTU.")

#     def mostrar_cor(self):
#         print(f"{self.cor} Selecionado.")


# meu_ar_condicionado = Arcondicionado(
#     cor="Branco",
#     potencia=12000,
#     temperatura=26, 
#     modo="resfriar",
#     estado="ligado"
# )

# meu_ar_condicionado.mostrar_temperatura()
# meu_ar_condicionado.modo_ar() 
# meu_ar_condicionado.ligar() 
# meu_ar_condicionado.mostrar_cor()
# meu_ar_condicionado.mostrar_potencia()


#segundoexercicio2
#Crie uma classe pessoa com os atributos nome e idade. Depois, crie 2 objetos dessa classe e mostre na tela o nome e a idade de cada pessoa


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
        
        
#     def mostrar(self):
#         print(f"Nome: {self.nome}, e Idade: {self.idade} anos.")
        
#     def aniversario(self):
#         print(f"Parabens {self.nome} , agora você tem {self.idade+1} anos.")


# P1 = Pessoa("Rodrigo", 30)
# P1.mostrar()
# P1.aniversario()

# P2 = Pessoa("Sabrina", 29)
# P2.mostrar()
# P2.aniversario()

# P3 = Pessoa("Hayssa", 21)
# P3.mostrar()

