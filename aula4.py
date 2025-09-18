#atividade1
 #Elabore um programa que imprima os números pares entre 1 e 20.

#resolução:

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#ATIVIDADE 2

#Elabore um programa para iterar sobre a palavra Python e imprimir letra por letra.

#RESOLUÇÃO:
palavra = "Python"
for letra in palavra:
    print(letra)

#ATIVIDADE 3

#Elabore um programa que preencha uma matriz de ordem 10 usando os indices i e j.

#RESOLUÇÃO:
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(i * j)
    matriz.append(linha)

for linha in matriz:
    print(linha)


#ATIVIDADE 4

#Elabore um programa que imprima a diagonal principal de uma matriz de ordem 10.

#RESOLUÇÃO:
ordem = 10
for i in range(ordem):
    for j in range(ordem):
        if i == j:
            print(f"Elemento na posição [{i},{j}]: {i * j}")

#ATIVIDADE 5
#Elabore um programa que imprima os números acima da diagonal principal de uma matriz de ordem 10.

#RESOLUÇÃO:
for i in range(ordem):
    for j in range(ordem):
        if j > i:
            print(f"Elemento acima da diagonal principal na posição [{i},{j}]: {i * j}")

#ATIVIDADE 6
# Elabore um programa que imprima os  números abaixo da diagonal principal de uma matriz de ordem 10.

#RESOLUÇÃO:
ordem = 10
for i in range(ordem):
    for j in range(ordem):
        if i > j:
            print(f"Elemento abaixo da diagonal principal na posição [{i},{j}]: {i * j}")  

#ATIVIDADE 7

#Elabore um programa que recebe um número e imprime a sua tabuada até 10.
#RESOLUÇÃO:
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
#ATIVIDADE 8
#Elabore um programa que recebe um número e imprime o seu fatorial.
#RESOLUÇÃO:
num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"O fatorial de {num} é: {fatorial}")


#ATIVIDADE 9
#Elabore um programa que recebe uma palavra e imprima quantas vogais ela possui.
#RESOLUÇÃO:
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador_vogais = 0
for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
print(f"A palavra '{palavra}' possui {contador_vogais} vogais.")

#ATIVIDADE 10
# Elabore um programa em Python que receba um número
# como entrada e imprima a soma dos números múltiplos de
# 5 até o número informado. O número deve ser maior que zero.

#RESOLUÇÃO:
num = int(input("Digite um número maior que zero: "))
if num > 0:
    soma_multiplos_5 = 0
    for i in range(1, num + 1):
        if i % 5 == 0:
            soma_multiplos_5 += i
    print(f"A soma dos múltiplos de 5 até {num} é: {soma_multiplos_5}")
else:
    print("Número inválido. Por favor, digite um número maior que zero.")
#ATIVIDADE 11

# Uma pesquisa coletou os seguintes dados:
# Hábito alimentar principal:
# 1- Fast-food | 2- Caseira | 3- Vegetariana | 4- Vegana | 5- Outros
# Pratica atividade física regularmente?
# 1- Sim | 2- Não
# Horas de sono por noite, Idade, Gênero (1- Feminino, 2- Masculino, 3- Outro).
# Peça N entrevistados e colete os dados N vezes. Informe:
# número de pessoas por hábito alimentar;
# média de horas de sono dos que comem fast-food;
# número de pessoas vegetarianas que praticam atividade física;
# número de pessoas veganas do gênero feminino;
# média de idade das pessoas que não praticam atividade física.

#RESOLUÇÃO:
num_entrevistados = int(input("Digite o número de entrevistados: "))
habito_alimentar = [0] * 5
soma_sono_fast_food = 0
contagem_fast_food = 0
contagem_vegetarianos_atividade = 0
contagem_veganas_feminino = 0
soma_idade_sem_atividade = 0
contagem_sem_atividade = 0
for _ in range(num_entrevistados):
    habito = int(input("Hábito alimentar (1- Fast-food, 2- Caseira, 3- Vegetariana, 4- Vegana, 5- Outros): "))
    atividade_fisica = int(input("Pratica atividade física regularmente? (1- Sim, 2- Não): "))
    horas_sono = float(input("Horas de sono por noite: "))
    idade = int(input("Idade: "))
    genero = int(input("Gênero (1- Feminino, 2- Masculino, 3- Outro): "))

    if 1 <= habito <= 5:
        habito_alimentar[habito - 1] += 1

    if habito == 1:
        soma_sono_fast_food += horas_sono
        contagem_fast_food += 1

    if habito == 3 and atividade_fisica == 1:
        contagem_vegetarianos_atividade += 1

    if habito == 4 and genero == 1:
        contagem_veganas_feminino += 1

    if atividade_fisica == 2:
        soma_idade_sem_atividade += idade
        contagem_sem_atividade += 1
print("Número de pessoas por hábito alimentar:")
print(f"Fast-food: {habito_alimentar[0]}")
print(f"Caseira: {habito_alimentar[1]}")
print(f"Vegetariana: {habito_alimentar[2]}")
print(f"Vegana: {habito_alimentar[3]}")
print(f"Outros: {habito_alimentar[4]}")
if contagem_fast_food > 0:
    media_sono_fast_food = soma_sono_fast_food / contagem_fast_food
    print(f"Média de horas de sono dos que comem fast-food: {media_sono_fast_food:.2f}")
else:
    print("Nenhum entrevistado informou comer fast-food.")
print(f"Número de pessoas vegetarianas que praticam atividade física: {contagem_vegetarianos_atividade}")
print(f"Número de pessoas veganas do gênero feminino: {contagem_veganas_feminino}")
if contagem_sem_atividade > 0:
    media_idade_sem_atividade = soma_idade_sem_atividade / contagem_sem_atividade
    print(f"Média de idade das pessoas que não praticam atividade física: {media_idade_sem_atividade:.2f}")
else:
    print("Nenhum entrevistado informou não praticar atividade física.")
