frutas = ["banana", "maça", "pera"]

print = (frutas[0]) #banana
print = (frutas[-1]) #pera

#modifica elementos
frutas[1] = "uva"

#Inserir elementos
frutas.append("abacaxi")
frutas.insert(1, "manga")

#remove elementos
frutas.remove("maça")
ultimo = frutas.pop()


frutas1 = ["maça", "banana", "laranja", "uva", "abacaxi", "manga"]
#fatiando do inicio até o indice 3 
print("Primeiros 3 elementos:", frutas1[:3])

#Fatiando do indice 2 até o final
print("DO indice 2 ate o final:", frutas1[2:])

#fatiando do indice 1 ao 4
print("Do indice 1 ao 3:", frutas1[1:4])

#Fatiando com passo
print("Elemebtos de 2 em 2:", frutas1[::2])

#fatiando ao contrario
print("Lista invertida:", frutas1[::-1])

#fatiando parte ao contrario
print("Ultimos 4 elementos invertidos:", frutas1[-1:-5:-1])


#Exemplo

frutas1 = ["maça", "banana", "laranja", "uva", "abacaxi", "manga"]

print("Loop FOR Simples:")
for frutas in frutas1:
    print(frutas)


print("\nLoop WHILE:")
i = 0 
while i < len(frutas1):
    print(frutas1[i])
    i += 1


atividade1

uma loja deseja monitorar o estoque de 6 produtos; escreva um programa que receba
do usuario os nomes dos produtos e a quantidade em estoque de cada um, crie uma litsa
de listas onde a primeira coluna é o nome do produto e a segunda a quantidade, e
depois substitua todas as quantidades menores que 10 por "estoque baixo" 
imprimindo a lista final.


qtd_produtos = 6

inicio_estoque = []

print("---Entrada de produtos---")

for i in range(qtd_produtos):
    while True:
        nome = input(f"Digite o nome do produto {i+1}: ").strip ()
        if nome:
            break
        else:
            ("Nome não pode ser vazio")

    while True:
        try:
            quantidade = int(input(f"Digite a quantidade em estoque de '{nome}': "))
            if quantidade >= 0: 
                break
            else:
                print("Não pode ser um numero negativo")
        except ValueError:
            print("Digite um número inteiro para a quantidade.")

    inicio_estoque.append([nome, quantidade])

print("\n--- Estoque Inicial Registrado ---")
print(inicio_estoque)
print("-" * 35)


estoque_final = []


for produto in inicio_estoque:
    nome_produto = produto[0]
    quantidade_produto = produto[1]

    if quantidade_produto < 10:
        novo_status = "estoque baixo"
    else:
        novo_status = quantidade_produto

    estoque_final.append([nome_produto, novo_status])

print("\n--- Estoque Final Monitorado ---")


print(estoque_final)

print("\n--- Lista final ---")
for item in estoque_final:
    print(f"Produto: {item[0]:<15} | Status: {item[1]}")

exercicio2
Um campeonato de futebol registrou os gols de 4 times em 5 partidas
cada. Escreva um programa que:
1 - Receba o nome de cada time.
2 - O número de gols marcados em cada partida por cada time.
3 - Calcule a proporção de partidas com gols ≥ 2 para cada time.
4 - Imprima o nome do time e a proporção em porcentagem.
5 - Indique quantos times tiveram proporção maior ou igual a 60%.


n_time = 4
n_partida = 5
gol_minimos = 2




resultados_finais = []
time_proporcao_alta = 0

print("--- REGISTRO DE GOLS DO CAMPEONATO COMPENSAAA ---")

for i in range(n_time):
    time = input(f"\nDigite o nome do time {i + 1}: ").strip()
    
    partida_mais_gols = 0
    
    print(f"--- Gols do {time} em 5 partidas ---")
    
    for j in range(n_partida):
        while True:
            try:
                gols = int(input(f"Partida {j + 1} - Gols marcados: "))
                if gols >= 0:
                    break
                else:
                    print("Gols não podem ser negativos ZEEEEE")
            except ValueError:
                print("Entrada inválida. somente numero inteiroooooo")
        
        if gols >= gol_minimos:
            partida_mais_gols += 1
            
    proporcao = (partida_mais_gols / n_partida) * 100
    
    resultados_finais.append((time, proporcao))



    
    if proporcao >= 60:
        time_proporcao_alta += 1

print("\n" + "=" * 40)
print("--- RESULTADO FINAL DO CAMPEONATO ---")
print("=" * 40)

for time, proporcao in resultados_finais:
    print(f"Time: {time:<15} | Proporção de jogos com 2+ gols: {proporcao:.2f}%")

print("-" * 40)
print(f"Total de times com proporção maior ou igual a 60%: **{time_proporcao_alta}**")
print("=" * 40)



