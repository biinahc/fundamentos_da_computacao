#exercicio1

class Prato:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        self.disponivel = True

    def exibir(self):
        print(self.nome, "- R$", self.preco)

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def indisponibilizar(self):
        self.disponivel = False


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar(self, prato):
        if prato.disponivel:
            self.itens.append(prato)
        else:
            print(prato.nome, "está indisponível.")

    def total(self):
        soma = 0
        for prato in self.itens:
            soma += prato.preco
        return soma


p1 = Prato("Arroz com frango", 18.0)
p2 = Prato("Macarrão", 15.0)
p3 = Prato("Suco de laranja", 7.0)

p3.alterar_preco(9.0)

p2.indisponibilizar()

pedido = Pedido()
pedido.adicionar(p1)
pedido.adicionar(p2) 
pedido.adicionar(p3) 

print("Itens do pedido:")
for item in pedido.itens:
    item.exibir()

print("Total do pedido: R$", pedido.total())

#exercicio2
class Prato:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class Restaurante:
    def __init__(self, nome: str):
        self.nome = nome
        self.cardapio = []
        self.pedidos = []

    def __str__(self):
        return f"Restaurante: {self.nome} | Total de pratos: {len(self)}"

    def __len__(self):
        return len(self.cardapio)

    def adicionar_prato(self, prato: Prato):
        self.cardapio.append(prato)

    def listar_cardapio(self):
        print(f"\n Cardápio de {self.nome}:")
        for i, prato in enumerate(self.cardapio, start=1):
            print(f"{i}. {prato}")

    def atender_cliente_por_numero(self, nome_cliente: str):
        while True:
            try:
                numero = int(input("Digite o número do prato desejado: "))
                if 1 <= numero <= len(self.cardapio):
                    prato = self.cardapio[numero - 1]
                    print(f"\n{nome_cliente}, seu pedido de '{prato.nome}' foi confirmado!")
                    print(f"Total a pagar: R$ {prato.preco:.2f}")
                    self.pedidos.append({
                        "cliente": nome_cliente,
                        "prato": prato.nome,
                        "valor": prato.preco
                    })
                    break
                else:
                    print("Escolha um número do cardápio.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")
    
    def listar_pedidos(self):
        print(f"\nPedidos realizados")
        if not self.pedidos:
            print("Nenhum Pedido foi feito ainda!")
        else:
            for i, pedido in enumerate(self.pedidos, start=1):
                print(f"{i}. Cliente: {pedido['cliente']} | Prato: {pedido['prato']} | Valor: R$ {pedido['valor']:.2f} ")
     
restaurante = Restaurante("Sabor Caseiro")
restaurante.adicionar_prato(Prato("Feijoada", 25.00))
restaurante.adicionar_prato(Prato("Lasanha", 22.50))
restaurante.adicionar_prato(Prato("Bife acebolado", 20.00))

def menu():
    while True:
        print("\n=== Bem-vindo ao Sabor Caseiro 😁 ===")
        print("1. Ver cardápio")
        print("2. Fazer pedido")
        print("3. Ver pedidos realizados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            restaurante.listar_cardapio()

        elif opcao == "2":
            nome = input("Digite seu nome: ")
            restaurante.listar_cardapio()
            restaurante.atender_cliente_por_numero(nome)
            
        elif opcao == "3":
            restaurante.listar_pedidos()

        elif opcao == "4":
            print("👋 Obrigado por visitar o Sabor Caseiro. Volte logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()


#exercicio3

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_de_livros = []

    def __str__(self):
        return f"Biblioteca: {self.nome} | Total de livros: {len(self)}"

    def __len__(self):
        return len(self.lista_de_livros)

    def adicionar_livro(self, titulo: str):
        self.lista_de_livros.append(titulo)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        print(f"\nLivros cadastrados na biblioteca '{self.nome}':")
        if not self.lista_de_livros:
            print("Nenhum livro cadastrado ainda.")
        else:
            for i, livro in enumerate(self.lista_de_livros, start=1):
                print(f"{i}. {livro}")


biblioteca = Biblioteca("Central de Leitura")

def menu_biblioteca():
    while True:
        print("\n=== Sistema da Biblioteca ===")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ver resumo da biblioteca")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            biblioteca.adicionar_livro(titulo)

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            print(biblioteca)

        elif opcao == "4":
            print("Encerrando o sistema da biblioteca. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu_biblioteca()

#exercicio4

class Aluno:
    def __init__(self, nome: str, idade: int, curso: str):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"


class Escola:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_de_alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.lista_de_alunos.append(aluno)
        print(f"Aluno '{aluno.nome}' matriculado com sucesso!")

    def listar_alunos(self):
        print(f"\nAlunos matriculados na escola '{self.nome}':")
        if not self.lista_de_alunos:
            print("Nenhum aluno matriculado ainda.")
        else:
            for i, aluno in enumerate(self.lista_de_alunos, start=1):
                print(f"{i}. {aluno.apresentar()}")

    def __len__(self):
        return len(self.lista_de_alunos)


escola = Escola("Escola Tecnologia")

def nome_valido(nome: str) -> bool:
    return nome.replace(" ", "").isalpha()

def idade_valida(idade: str) -> bool:
    return idade.isdigit()



def menu_escola():
    while True:
        print("\n=== Sistema de Cadastro de Alunos ===")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Ver total de alunos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                nome = input("Digite o nome do aluno: ")
                if nome_valido(nome):
                    break
                else:
                    print("Nome inválido. Não use números ou símbolos.")

            while True:
                idade_input = input("Digite a idade do aluno: ")
                if idade_valida(idade_input):
                    idade = int(idade_input)
                    break
                else:
                    print("Idade inválida. Digite apenas números.")

            curso = input("Digite o curso do aluno: ")
            novo_aluno = Aluno(nome, idade, curso)
            escola.adicionar_aluno(novo_aluno)

        elif opcao == "2":
            escola.listar_alunos()

        elif opcao == "3":
            print(f"Total de alunos na escola: {len(escola)}")

        elif opcao == "4":
            print("Até mais!")
            break

        else:
            print("Opção inválida.")

menu_escola()




