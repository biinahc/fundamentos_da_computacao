#exercicio1

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"{self.nome} foi aprovado com média {media:.2f}."
        else:
            return f"{self.nome} foi reprovado com média {media:.2f}."


aluno1 = Aluno("Ana", 8.5, 7.0)
aluno2 = Aluno("Bruno", 6.0, 5.5)

print(aluno1.verificar_aprovacao())
print(aluno2.verificar_aprovacao())

#exercicio2

class Paciente:
    def __init__(self, nome, idade, cpf, doenca):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.doenca = doenca

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Doença: {self.doenca}")
        print("-" * 30)

    def atualizar_doenca(self, nova_doenca):
        self.doenca = nova_doenca


paciente1 = Paciente("Sabrina", 45, "123.456.789-00", "Colica")
paciente2 = Paciente("Hayssa", 30, "987.654.321-00", "Gripe")

paciente1.exibir_dados()
paciente2.exibir_dados()

paciente2.atualizar_doenca("Sinusite")

print("Após atualização da doença:")
paciente2.exibir_dados()