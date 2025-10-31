class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if novo_nome: self.__nome = novo_nome

    def adicionar_livro(self, titulo):
        if titulo and titulo not in self.__livros: self.__livros.append(titulo)

    def listar_livros(self):
        print("Livros:" if self.__livros else "Nenhum livro cadastrado.")
        for livro in self.__livros: print("-", livro)

b = Biblioteca("Biblioteca Central")
for l in ["Dom Casmurro", "1984", "O Pequeno Príncipe"]: b.adicionar_livro(l)
b.adicionar_livro("1984")
b.listar_livros()
b.set_nome("Biblioteca Municipal")
print("Novo nome:", b.get_nome())