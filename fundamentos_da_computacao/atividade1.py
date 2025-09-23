onibus = 0
carro = 0
moto = 0
bicicleta = 0
outros = 0
gastos_bicicleta = 0
total_bike = 0
norte_outros = 0
sul_carro = 0
soma_idade1 = 0
total_mulheres_onibus = 0
nomes_entrevistados = []


menu_transporte = """
Meio de transporte principal:
[1] Ônibus
[2] Carro
[3] Moto
[4] Bicicleta
[5] Outros
[0] Sair
"""

while True:
    print("\n--- Cadastro do Participante 😁 ---")
    
    transporte = input(menu_transporte + "\nEscolha uma opção: ")

    if not transporte.isdigit():
        print("Entrada inválida! Digite um número.")
        continue

    transporte = int(transporte)

    if transporte == 0:
        break
    elif 1 <= transporte <= 5:
        print("\nVamos para a próxima pergunta 😊")
    else:
        print("Escolha de 1 a 5 apenas! 😒")

    def obter_zona():
        while True:
            try:
                zona = int(input("Qual sua Zona de moradia:\n 1- Zona Norte\n 2- Zona Sul \n 3- Outros\nOpção: "))
                if zona in [1, 2, 3]:
                    return zona
                print("Opção inválida! Por favor, escolha um número de 1 a 3.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

    zona = obter_zona()
    print("\nVamos para a proxima pergunta😊" )

    while True:
        try:
            gasto = float(input("Qual seu Gasto Mensal com transporte (R$): "))
            if gasto >= 0:
                break
            else:
                print("O gasto não pode ser negativo. Digite novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

    print("\nVamos para a proxima pergunta😊" )

    while True:
        try:
            idade = int(input("Qual sua Idade: "))
            if idade > 130:
                print("Diga uma idade realista.")
            elif idade > 0:
                break
            else:
                print("A idade precisa ser maior que zero. Digite novamente.")
        except ValueError:
            print("Digite um numero valido.")



    while True:
        nome = input("Qual seu nome: ")

        if isinstance(nome, str):
            nomes_entrevistados.append(nome)
            break

        else:
            print("Entrada inválida. O nome deve ser uma string.")


    while True:
        try:
            genero = int(input("Gênero:\n1 - Feminino\n2- Masculino\n3- Outro\nOpção: "))
            if 1 <= genero <= 3:
                break
            else:
                print("Escolha uma opção de 1 à 3.")
        except ValueError:
            print("Digite um número válido.")

    if transporte == 1:
        onibus += 1
        if genero == 1:
            soma_idade1 += idade
            total_mulheres_onibus += 1
    elif transporte == 2:
        carro += 1
        if zona == 2:
            sul_carro += 1
    elif transporte == 3:
        moto += 1
    elif transporte == 4:
        bicicleta += 1
        gastos_bicicleta += gasto
        total_bike += 1
    elif transporte == 5:
        outros += 1
        if zona == 1:
            norte_outros += 1


media_gasto_bike = 0
if total_bike > 0:
    media_gasto_bike = gastos_bicicleta / total_bike

media_idade_mulheres_onibus = 0
if total_mulheres_onibus > 0:
    media_idade_mulheres_onibus = soma_idade1 / total_mulheres_onibus

print("\n--- Resumo ---")
print("Transporte:")
print("Ônibus:", onibus)
print("Carro:", carro)
print("Moto:", moto)
print("Bicicleta:", bicicleta)
print("Outros:", outros)

print("\nGasto médio (bicicleta): R$", round(media_gasto_bike, 2))
print("Zona Norte com 'Outros':", norte_outros)
print("Zona Sul com 'Carro':", sul_carro)
print("Idade média (mulheres que usam ônibus):", round(media_idade_mulheres_onibus, 2))

print("\nEntrevistados:")
for i, nome in enumerate(nomes_entrevistados, start=1):
    print(f"{i} - {nome}")

print("\nFim da pesquisa.")