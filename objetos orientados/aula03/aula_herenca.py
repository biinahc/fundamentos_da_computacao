# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# class Aluno(Pessoa):
#     def __init__(self, nome, matricula):
#         super().__init__(nome)
#         self.matricula = matricula



# aluno_sabrina = Aluno("Joao", 123)
    
# print(f"Nome do aluno: {aluno_sabrina.nome}")
# print(f"Matricula do aluno: {aluno_sabrina.matricula}")

# class Veiculo:
#     def __init__(self, marca):
#         self.marca = marca

# class Carro(Veiculo):
#     def __init__(self, marca, modelo):
#         super().__init__(marca)
#         self.modelo = modelo



# carro1 = Carro("Chevrolet", "Onix Turbo")


# print(f"Marca: {carro1.marca}")
# print(f"Modelo: {carro1.modelo}")



# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

#     def falar(self):
#         print(f"{self.nome} está falando.")

# class Professor(Pessoa):
#     def __init__(self, nome, disciplina):
#         super().__init__(nome) 
#         self.disciplina = disciplina

#     def falar(self):
#         print(f"Professor(a){self.nome} está ensinando {self.disciplina}.")

# class Aluno(Pessoa):
#     def __init__(self, nome, matricula):
#         super().__init__(nome) 
#         self.matricula = matricula

#     def falar(self):
#         print(f"Aluno(a){self.nome}, Matricula {self.matricula} está aprendendo.")


# pessoa1 = Pessoa ("Maria")
# professor1 = Professor("Carlos", "Matematica")
# aluno1 = Aluno ("Ana", 101)

# pessoa1.falar()
# professor1.falar()
# aluno1.falar()

# class Veiculo:
#     def __init__(self, marca):
#         self.marca = marca

# class Carro(Veiculo):
#     def __init__(self, marca, modelo):
#         super().__init__(marca)
#         self.modelo = modelo

# class Bolsista(Aluno):
#     def __init__(self, nome, matricula, bolsa):
#         super().__init__(nome, matricula)
#         self.bolsa = bolsa

# Criando um objeto da classe Bolsista
# carro1 = Carro("Chevrolet", "Onix Turbo")

# Imprimindo os dados
# print(f"Marca: {carro1.marca}")
# print(f"Modelo: {carro1.modelo}")
# print(f"Matrícula: {bolsista1.matricula}")
# print(f"Tipo de bolsa: {bolsista1.bolsa}")