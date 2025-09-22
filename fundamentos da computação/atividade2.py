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
        if total >= 10:
            print("Já tem 10 produtos cadastrados. Não é possível adicionar mais.")
        else:
            nome = input("Nome do produto: ")
            while True:
                try:
                    quantidade_adicionada = int(input("Quantidade: "))
                    if quantidade_adicionada < 0:
                        print("A quantidade não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Digite um número inteiro válido.")
            
            produtos[total] = nome
            qtd[total] = quantidade_adicionada
            total += 1
            print("Produto adicionado com sucesso!")

    elif opcao == 2:
        if total == 0:
            print("Não há produtos cadastrados para alterar.")
            continue
        
        print("\nProdutos cadastrados:")
        for i in range(total):
            print(f"{i} - {produtos[i]} ({qtd[i]} unidades)")
        
        try:
            id_alterar = int(input("Digite o ID do produto para alterar a quantidade: "))
            
            if 0 <= id_alterar < total:
                while True:
                    try:
                        nova_quantidade = int(input(f"Nova quantidade para {produtos[id_alterar]}: "))
                        if nova_quantidade < 0:
                            print("A quantidade não pode ser negativa. Tente novamente.")
                            continue
                        break
                    except ValueError:
                        print("Digite um número inteiro válido.")
                
                qtd[id_alterar] = nova_quantidade
                print("Quantidade atualizada com sucesso!")
            else:
                print("ID inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número para o ID.")

    elif opcao == 3:
        if total == 0:
            print("Não há produtos cadastrados para remover.")
            continue
        
        print("\nUse a opção 4 para ver os IDs dos produtos.")
        try:
            id_remover = int(input("ID do produto para remover: "))
            
            if 0 <= id_remover < total:
                for i in range(id_remover, total - 1):
                    produtos[i] = produtos[i + 1]
                    qtd[i] = qtd[i + 1]
                
                produtos[total - 1] = None
                qtd[total - 1] = 0
                total -= 1
                print("Produto removido com sucesso!")
            else:
                print("ID inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número para o ID.")

    elif opcao == 4:
        if total == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\nProdutos:")
            for i in range(total):
                print(f"{i} - {produtos[i]} ({qtd[i]} unidades)")
            
    elif opcao == 5:
        busca = input("Nome do produto: ")
        achou = False
        for i in range(total):
            if produtos[i] and produtos[i].lower() == busca.lower():
                print(f"{i} - {produtos[i]} ({qtd[i]} unidades)")
                achou = True
                break
        if not achou:
            print("Produto não encontrado.")

    elif opcao == 6:
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Escolha entre 1 e 6.")
