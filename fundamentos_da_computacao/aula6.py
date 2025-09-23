#atividade1

# Elabore um programa que crie um vetor de 10 números, encontre o
# maior, menor e a soma de todos os elementos. Por fim, o programa
# deve dizer se um número dito pelo usuário está presente no vetor ou
# não.

#resolução:
import numpy as np
vetor = np.random.randint(1, 100, 10)
print("Vetor:", vetor)
maior = vetor [0]
menor = vetor [0]
soma = 0
for num in vetor:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma dos elementos:", soma)
num_usuario = int(input("Digite um número para verificar se está no vetor: "))
if num_usuario in vetor:
    print(f"O número {num_usuario} está presente no vetor.")
else:
    print(f"O número {num_usuario} não está presente no vetor.")

#ATIVIDADE 2

# Elabore um programa que receba as notas de 5 alunos, armazene-as em um vetor e calcule a média das notas.

#RESOLUÇÃO:
notas = np.zeros(5)
for i in range(5):
    notas[i] = float(input(f"Digite a nota do aluno {i + 1}: "))
media = np.mean(notas)
print("Média das notas:", media)
print("Notas dos alunos:", notas)

#ATIVIDADE 3
# Elabore um programa que receba os nomes de 5 alunos, armazene-as
# em um vetor e imprima apenas os nomes que possuem mais de 5 caracteres.
#RESOLUÇÃO:
nomes = []
for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nomes.append(nome)
print("Nomes com mais de 5 caracteres:")
for nome in nomes:
    if len(nome) > 5:
        print(nome)


#ATIVIDADE 4
# Elabore um programa que receba 10 números, armazene-os em um
# vetor, inverta a ordem dos números e imprima o vetor invertido.

#RESOLUÇÃO:
numeros = []
for i in range(10):
    num = int(input(f"Digite o número {i + 1}: "))
    numeros.append(num)
numeros_invertidos = numeros[::-1]
print("Vetor invertido:", numeros_invertidos)

#ATIVIDADE 5
# Leia 8 temperaturas em °C para um array, converta os valores para °F,
# e exiba a média, o mínimo e o máximo em ambas as escalas.

#RESOLUÇÃO:
temperaturas_c = []
for i in range(8):
    temp_c = float(input(f"Digite a temperatura {i + 1} em °C: "))
    temperaturas_c.append(temp_c)
temperaturas_f = [(temp * 9/5) + 32 for temp in temperaturas_c]
media_c = np.mean(temperaturas_c)
media_f = np.mean(temperaturas_f)
min_c = np.min(temperaturas_c)
min_f = np.min(temperaturas_f)
max_c = np.max(temperaturas_c)
max_f = np.max(temperaturas_f)
print(f"Média: {media_c:.2f} °C, {media_f:.2f} °F")
print(f"Mínimo: {min_c:.2f} °C, {min_f:.2f} °F")
print(f"Máximo: {max_c:.2f} °C, {max_f:.2f} °F")

#ATIVIDADE 6

# Elabore um programa que receba um vetor com 10 números e ordene
# do maior para o menor.
#RESOLUÇÃO:
numeros = []
for i in range(10):
    num = int(input(f"Digite o número {i + 1}: "))
    numeros.append(num)
numeros_ordenados = sorted(numeros, reverse=True)
print("Vetor ordenado do maior para o menor:", numeros_ordenados)


#ATIVIDADE 7
# A concessionária local de telefonia de uma cidade do interior de

# Manaus gostaria de um programa que pudesse controlar a central de
# 10 assinantes que foi disponibilizada para a cidade. Desenvolva um
# programa com o menu a seguir:

# 1. Inclusão de novo telefone

# 2. Alteração de telefone
# 3. Exclusão de telefone

# 4. Impressão dos telefones cadastrados
# 5. Consulta por nome
# 6. Sair

#RESOLUÇÃO:
telefones = {}
while True:
    print("\nMenu:")
    print("1. Inclusão de novo telefone")
    print("2. Alteração de telefone")
    print("3. Exclusão de telefone")
    print("4. Impressão dos telefones cadastrados")
    print("5. Consulta por nome")
    print("6. Sair")
    opcao = input("Escolha uma opção (1-6): ")
    
    if opcao == '1':
        if len(telefones) < 10:
            nome = input("Digite o nome do assinante: ")
            telefone = input("Digite o número de telefone: ")
            telefones[nome] = telefone
            print(f"Telefone de {nome} adicionado.")
        else:
            print("Limite de 10 assinantes atingido.")
    
    elif opcao == '2':
        nome = input("Digite o nome do assinante para alterar o telefone: ")
        if nome in telefones:
            novo_telefone = input("Digite o novo número de telefone: ")
            telefones[nome] = novo_telefone
            print(f"Telefone de {nome} alterado.")
        else:
            print(f"Assinante {nome} não encontrado.")
    
    elif opcao == '3':
        nome = input("Digite o nome do assinante para excluir o telefone: ")
        if nome in telefones:
            del telefones[nome]
            print(f"Telefone de {nome} excluído.")
        else:
            print(f"Assinante {nome} não encontrado.")
    
    elif opcao == '4':
        if telefones:
            print("Telefones cadastrados:")
            for nome, telefone in telefones.items():
                print(f"{nome}: {telefone}")
        else:
            print("Nenhum telefone cadastrado.")
    
    elif opcao == '5':
        nome = input("Digite o nome do assinante para consulta: ")
        if nome in telefones:
            print(f"{nome}: {telefones[nome]}")
        else:
            print(f"Assinante {nome} não encontrado.")
    
    elif opcao == '6':
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")


        
