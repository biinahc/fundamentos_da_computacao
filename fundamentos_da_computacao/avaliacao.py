from collections import deque

custo = [[10, 12, 15], [11, 13, 14], [9, 10, 11]]
capacidade = [[200, 150, 180], [160, 170, 190], [140, 130, 120]]
expedidas = [[0]*3 for _ in range(3)]

fila = deque()
historico = []

custo_rota = [[0]*3 for _ in range(3)]
custo_deposito = [0]*3
custo_loja = [0]*3
total = 0
urgentes = normais = risco = 0

print("="*40)
print("Navega Amazônia Sistema de Expedição")
print("="*40)

while True:
    op = input("\n1-Pedido  2-Expedir  3-Próximo  4-Desfazer  5-Relatórios  6-Sair: ")

    if op == "1":
        codigo = input("Código: ")
        urg = input("Urgente (U/N): ").upper()
        peso = float(input("Peso (kg): "))
        qtd = int(input("Qtd caixas: "))

        while True:
            d = int(input("Depósito (1-3): ")) - 1
            if d in [0, 1, 2]: break
            print("Depósito inválido. Tente novamente.")

        while True:
            l = int(input("Loja (1-3): ")) - 1
            if l in [0, 1, 2]: break
            print("Loja inválida. Tente novamente.")

        risco_flag = peso > 20 or qtd > 100
        custo_estimado = qtd * custo[d][l]
        pedido = [codigo, urg, peso, qtd, d, l, custo_estimado, risco_flag]

        if urg == "U":
            fila.appendleft(pedido)
        elif peso <= 5:
            fila.append(pedido)
        elif peso >= 20:
            fila.append(pedido)
        else:
            fila.append(pedido)

        print("Pedido registrado.")

    elif op == "2":
        if not fila:
            print("Fila vazia.")
            continue

        p = fila.popleft()
        codigo, urg, peso, qtd, d, l, custo_estimado, risco_flag = p

        if capacidade[d][l] < qtd:
            print("Capacidade insuficiente.")
            fila.appendleft(p)
            continue

        capacidade[d][l] -= qtd
        expedidas[d][l] += qtd
        custo_rota[d][l] += custo_estimado
        custo_deposito[d] += custo_estimado
        custo_loja[l] += custo_estimado
        total += custo_estimado
        if urg == "U": urgentes += 1
        else: normais += 1
        if risco_flag: risco += 1
        historico.append(p)
        print(f"Pedido {codigo} expedido.")

    elif op == "3":
        print("Próximo:", fila[0][0] if fila else "Fila vazia.")

    elif op == "4":
        if not historico:
            print("Nada para desfazer.")
            continue

        p = historico.pop()
        codigo, urg, peso, qtd, d, l, custo_estimado, risco_flag = p
        capacidade[d][l] += qtd
        expedidas[d][l] -= qtd
        custo_rota[d][l] -= custo_estimado
        custo_deposito[d] -= custo_estimado
        custo_loja[l] -= custo_estimado
        total -= custo_estimado
        if urg == "U": urgentes -= 1
        else: normais -= 1
        if risco_flag: risco -= 1
        fila.appendleft(p)
        print(f"Pedido {codigo} desfeito.")

    elif op == "5":
        print("\nRelatórios")
        print("a) Custo por rota:")
        for r in custo_rota: print(r)
        print("b) Custo por depósito:", custo_deposito)
        print("c) Custo por loja:", custo_loja)
        print("d) Custo total:", total)
        print("e) Urgentes:", urgentes, "Normais:", normais, "Com risco:", risco)

    elif op == "6":
        print("Saindo...")
        break