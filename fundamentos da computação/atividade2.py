produtos = [None] * 10
qtd = [0] * 10
total = 0
menu = """
--- Mercearia da Sabrina ---
[1] Adicionar produto
[2] Alterar quantidade
[3] Remover produto
[4] Ver produtos
[5] Buscar produto
[6] Sair
"""

while True:
    print(menu)
    escolha = input("Escolha uma opção: ")

    if not escolha.isdigit():
        print("Digite um número válido.")
        continue

    opcao = int(escolha)

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        pass
    elif opcao == 6:
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Escolha entre 1 e 6.")

    try:
        opcao = int(input("Escolha uma opção: "))
    except:
        print("Digite um número válido.")
        continue

    if opcao == 1:
        if total >= 10:
            print("Já tem 10 produtos cadastrados.")
        
        else:
            nome = input("Nome do produto: ")
            while True:
                try:
                    qtd = int(input("Quantidade: "))
                    break
                except:
                    print("Digite um número inteiro.")
            produtos[total] = nome
            qtd[total] = qtd
            total += 1
            print("Produto adicionado!")

    elif opcao == 2:
        print("\nProdutos cadastrados:")
        for i in range(total):
            if produtos[i] != None:
                print(f"{i} - {produtos[i]} ({qtd[i]} unidades)")

        id = input("Digite o ID do produto: ")

        if id.isdigit():
            id = int(id)
            if id >= 0 and id < total and produtos[id] != None:
                while True:
                    nova = input("Nova quantidade: ")
                    if nova.isdigit():
                        nova = int(nova)
                        if nova < 0:
                            print("Quantidade não pode ser negativa. Tente novamente.")
                        elif nova == qtd[id]:
                            print("Essa quantidade já está em estoque. Nenhuma alteração feita.")
                            break
                        else:
                            qtd[id] = nova
                            print("Quantidade atualizada.")
                            break
                    else:
                        print("Digite um número inteiro.")
            else:
                print("ID inválido.")
        else:
            print("ID inválido.")

    elif opcao == 3:
        print("Use a opção 4 para ver os IDs dos produtos.")
        try:
            id = int(input("ID do produto para remover: "))
            if 0 <= id < total and produtos[id] != None:
                for i in range(id, total - 1):
                    produtos[i] = produtos[i + 1]
                    qtd[i] = qtd[i + 1]
                produtos[total - 1] = None
                qtd[total - 1] = 0
                total -= 1
                print("Produto removido.")
            else:
                print("ID inválido.")
        except:
            print("Entrada inválida.")

    elif opcao == 4:
        print("\nProdutos:")
        for i in range(total):
            print(f"{i} - {produtos[i]} ({qtd[i]} unidades)")
            
    elif opcao == 5:
        busca = input("Nome do produto: ")
        achou = False
        for i in range(total):
            if produtos[i] == busca:
                print(f"{i} - {produtos[i]} ({qtd[i]} unidades)")
                achou = True
                break
        if not achou:
            print("Produto não encontrado.")

    elif opcao == 6:
        print("Tchau! Obrigado por usar o programa ❤️.")
        break

    else:
        print("Opção inválida.")