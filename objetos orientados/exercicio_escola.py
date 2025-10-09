class Aluno:
    def __init__(self, nome, idade, curso):
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso

    def get_nome(self): return self.__nome
    def set_nome(self, n): 
        if n: self.__nome = n
    def get_idade(self): return self.__idade
    def set_idade(self, i): 
        if i > 0: self.__idade = i
    def get_curso(self): return self.__curso
    def set_curso(self, c):
        if c: self.__curso = c
    def apresentar(self): return f"Nome: {self.__nome} | Idade: {self.__idade} | Curso: {self.__curso}"

class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    def get_nome(self): return self.__nome
    def set_nome(self, n): 
        if n: self.__nome = n
    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno): self.__alunos.append(aluno)

    def listar_alunos(self):
        if not self.__alunos: print("Nenhum aluno matriculado.")
        else:
            for a in self.__alunos: print(a.apresentar())

# Teste
e = Escola("Escola Futuro")
a1 = Aluno("Sabrina", 29, "Informática")
a2 = Aluno("Hayssa", 18, "Enfermagem")
e.adicionar_aluno(a1)
e.adicionar_aluno(a2)
e.listar_alunos()
a1.set_nome("João Silva")
a2.set_idade(19)
a2.set_curso("Gestão")
print(a1.apresentar())
print(a2.apresentar())