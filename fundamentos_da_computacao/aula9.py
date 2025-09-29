from collections import deque

#Exercicio 2

livros_lista = []

for i in range(10):
    livro = input(f"Digite o nome do livro {i+1}: ")
    livros_lista.append(livro)

print("Livro no topo (lista):", livros_lista[-1])

livro_removido = livros_lista.pop()
print("Livro removido (lista):", livro_removido)

print("Pilha atual (lista):", livros_lista)


from collections import deque

livros_deque = deque()

for i in range(10):
    livro = input(f"Digite o nome do livro {i+1}: ")
    livros_deque.append(livro)

print("Livro no topo (deque):", livros_deque[-1])

livro_removido = livros_deque.pop()
print("Livro removido (deque):", livro_removido)

print("Pilha atual (deque):", list(livros_deque))


#exercicio 2

urls = deque()

while True:
    operacao = input("\n1-Visitar  2-Voltar  3-Atual  4-Sair: ")

    if operacao == "1":
        urls.append(input("URL: "))
    elif operacao == "2":
        print("Voltando de:", urls.pop() if urls else "Nada para voltar")
    elif operacao == "3":
        print("Atual:", urls[-1] if urls else "Nenhuma página")
    elif operacao == "4":
        break
    
#exercicio 3
pilha_pratos = deque()
limite_pratos = 5

while True:
    menu = input("\n 1-Adicionar 2-Retirar 3-Topo 4-Sair: ")

    if menu == "1":
        if len(pilha_pratos) < limite_pratos:
            prato = input("Nome do prato: ").strip()
            if pilha_pratos: limite_pratos(pilha_pratos)
            else: print("Não pode ser um prato vazioooo")
            
        else:
            print("Limite de prato, monte cheio")
    elif menu == "2":
        print("Retirado:", pilha_pratos.pop() if pilha_pratos else "Nada no monte")
    elif menu == "3":
        print("Topo:", pilha_pratos[-1] if pilha_pratos else "Monte vazio")
    elif menu == "4":
       break
   
#exercicio 4



fila = deque()

print("="*40)
print(" Fila de Atendimento Bancario")
print("="*40)
print("Escolha sua opção ")
while True:
    op = input("\n1-Adicionar  2-Atender  3-Frente  4-Sair: ")

    if op == "1":
        nome = input("Nome do Cliente: ").strip()
        idade = input("Idade do Cliente: ").strip()
        if nome and idade.isdigit():
            cliente = f"{nome} ({idade})"
            fila.appendleft(cliente) if int(idade) >= 60 else fila.append(cliente)
        else:
            print(" Dados Incorretos.")
    elif op == "2":
        print("Atendendo:", fila.popleft() if fila else "fila vazia.")
    elif op == "3":
        print("Frente:", fila[0] if fila else "fila vazia.")
    elif op == "4":
        break
    
    
#exercicio 5


fila = deque()

print("="*40)
print("Sistema de Fila de Pacientes da Clínica")
print("="*40)

while True:
    op = input("\n1-Adicionar  2-Atender  3-Próximo  4-Sair: ")

    if op == "1":
        nome = input("Nome do Paciente: ").strip()
        idade = input("Idade do Paciente: ").strip()
        agendado = input("Tem agendamento? (s/n): ").strip().lower()

        if not nome or not idade.isdigit() or agendado not in ["s", "n"]:
            print(" Dados inválidos.")
            continue

        idade = int(idade)
        paciente = f"{nome} ({idade} anos, {'agendado' if agendado == 's' else 'sem agendamento'})"

        if idade >= 60:
            fila.appendleft(paciente)
        elif agendado == "s":
            pos = next((i for i, p in enumerate(fila) if "60 anos" not in p), len(fila))
            fila.insert(pos, paciente)
        else:
            fila.append(paciente)

        print(f"Adicionado: {paciente}")
        print("Fila atual:", list(fila))

    elif op == "2":
        print("Atendendo:", fila.popleft() if fila else "Fila vazia.")
        print("Fila atual:", list(fila))

    elif op == "3":
        print("Próximo da fila:", fila[0] if fila else "Fila vazia.")
        print("Fila atual:", list(fila))

    elif op == "4":
        print("Encerrando atendimento... Obrigada por utilizar nosso Serviço!")
        break


    
            
