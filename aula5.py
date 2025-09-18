#atividade1

# Escreva um programa que utilize a estrutura while para somar todos
# os números pares de 1 até um número N informado pelo usuário.
# Utilize um contador para percorrer os números e verifique se cada
# número é par antes de somá-lo. Ao final, exiba a soma total.

#RESOLUÇÃO:
N = int(input("Digite um número inteiro positivo N: "))
soma = 0
contador = 1
while contador <= N:
    if contador % 2 == 0:
        soma += contador
    contador += 1
print(f"A soma de todos os números pares de 1 até {N} é: {soma}")

#ATIVIDADE 2
# Elabore um programa que some números até que o usuário digite 0 para sair.
#rESOLUÇÃO:
soma = 0
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero
print(f"A soma total dos números digitados é: {soma}")
#ATIVIDADE 3

# Elabore um programa que some números até que o usuário digite 0 para sair e que ignore números negativos.

#RESOLUÇÃO:
soma = 0
while True:
    numero = float(input("Digite um número positivo (ou 0 para sair): "))
    if numero == 0:
        break
    if numero < 0:
        print("Número negativo ignorado.")
        continue
    soma += numero
print(f"A soma total dos números positivos digitados é: {soma}")

#ATIVIDADE 4
# Simule um menu de opções que permita ao usuário escolher
# entre as seguintes opções:
# 1 - Dizer olá
# 2 - Dizer adeus
# 0 - Sair
# O programa deve repetir o menu até que o usuário escolha a opção de sair.

#RESOLUÇÃO:
while True:
    print("Menu de opções:")
    print("1 - Dizer olá")
    print("2 - Dizer adeus")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Olá!")
    elif escolha == "2":
        print("Adeus!")
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

#ATIVIDADE 5
# Elabore um jogo de adivinhação em que o computador escolhe um número aleatório
# entre 1 e 20 e o usuário deve tentar acertar. O programa deve continuar pedindo
# números até que o usuário acerte e direcionando se o número deve ser maior ou
# menor que o digitado. Dica: Use a função random.

#RESOLUÇÃO:
import random
numero_secreto = random.randint(1, 20)
tentativas = -1
print("Bem-vindo ao jogo de adivinhação!")
while True:
    palpite = int(input("Digite um número entre 1 e 20 (ou 0 para sair): "))
    if palpite == 0:
        print("Saindo do jogo. O número secreto era:", numero_secreto)
        break
    tentativas += 1
    if palpite < numero_secreto:
        print("Tente um número maior.")
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break

#ATIVIDADE 6
# Desenvolva uma calculadora interativa que permita ao usuário escolher a operação (+,
# -, *, /) e dois números. O programa deve repetir o menu até que o usuário escolha sair.

#RESOLUÇÃO:
while True:
    print("Calculadora Interativa")
    print("Escolha a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")
    escolha = input("Digite sua escolha: ")
    if escolha == "0":
        print("Saindo da calculadora.")
        break
    if escolha in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if escolha == "1":
            resultado = num1 + num2
            operacao = "+"
        elif escolha == "2":
            resultado = num1 - num2
            operacao = "-"
        elif escolha == "3":
            resultado = num1 * num2
            operacao = "*"
        elif escolha == "4":
            if num2 != 0:
                resultado = num1 / num2
                operacao = "/"
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue
        print(f"{num1} {operacao} {num2} = {resultado}")
    else:
        print("Opção inválida. Tente novamente.")


#ATIVIDADE 7
#Crie um programa que peça ao usuário um número inteiro positivo N e, em seguida,
# imprima a tabuada de 1 até 10 para esse número. Se o usuário digitar um número
# inválido (menor que 1), o programa deve pedir novamente até receber um número
# válido.

#RESOLUÇÃO:
n=0
while n < 1:
    n = int(input("Digite um número inteiro positivo N: "))
    if n < 1:
        print("Número inválido. Por favor, digite um número maior que zero.")
contador = 1
while contador <= 10:
    resultado = n * contador
    print(f"{n} x {contador} = {resultado}")
    contador += 1

#ATIVIDADE 8
# Elabore um algoritmo que leia um número inteiro e apresenta o fatorial desse número.
# O algoritmo se encerra quando se digitar um número menor que 1.

#RESOLUÇÃO:
numero = int(input("Digite um número inteiro positivo para calcular o fatorial (ou um número menor que 1 para sair): "))
while numero >= 1:
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial *= contador
        contador += 1
    print(f"O fatorial de {numero} é: {fatorial}")
    numero = int(input("Digite outro número inteiro positivo para calcular o fatorial (ou um número menor que 1 para sair): "))
print("Programa encerrado.")

#ATIVIDADE 9
# Elabore um programa que leia a idade de várias pessoas e imprima o total de pessoas
# maiores de idade e o total de pessoas menores de idade. O programa se encerra
# quando zero for passado.

#RESOLUÇÃO:
maiores_idade = 0
menores_idade = 0  
while True:
    idade = int(input("Digite a idade da pessoa (ou 0 para sair): "))
    if idade == 0:
        break
    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1
print(f"Total de pessoas maiores de idade: {maiores_idade}")
print(f"Total de pessoas menores de idade: {menores_idade}")

#ATIVIDADE 10
# Elabore um programa que receba números inteiros e diga se o número é primo ou
# não. O programa se encerra quando zero for passado.
#RESOLUÇÃO:
numero = int(input("Digite um número inteiro positivo para verificar se é primo (ou 0 para sair): "))
while numero != 0:
    if numero < 2:
        print(f"{numero} não é um número primo.")
    else:
        eh_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
    numero = int(input("Digite outro número inteiro positivo para verificar se é primo (ou 0 para sair): "))
print("Programa encerrado.")

#ATIVIDADE 7
# Uma das maneiras de se conseguir a raiz quadrada de um número é subtrair do
# número os ímpares consecutivos a partir de 1, até que o resultado da subtração seja
# menor ou igual a zero. O número de vezes que se conseguir fazer a subtração é a raiz
# quadrada exata do número, caso o resultado da subtração seja zero. Elabore um
# programa que calcula a raiz quadrada utilizando essa técnica.

#RESOLUÇÃO:
while numero != 0:
    if numero < 0:
        print("Número inválido. Por favor, digite um número não negativo.")
    else:
        subtracao = numero
        impar = 1
        contador = 0
        while subtracao >= 0:
            subtracao -= impar
            impar += 2
            if subtracao >= 0:
                contador += 1
        if subtracao == 0:
            print(f"A raiz quadrada exata de {numero} é: {contador}")
        else:
            print(f"{numero} não possui raiz quadrada exata.")
    numero = int(input("Digite outro número inteiro positivo para verificar a raiz quadrada (ou 0 para sair): "))
print("Programa encerrado.")

#atividade8
# Uma pesquisa de opinião realizada no Rio de Janeiro teve as seguintes perguntas:
# Qual seu time do coração?
# 1 - Flamengo
# 2 - Vasco
# 3 - Botafogo
# 4 - Fluminense
# 5 - Outros
# Onde você mora?
# 1 - Rio de Janeiro
# 2 - Niterói
# 3 - Outros
# Qual seu salário?
# Qual sua idade?
# Qual seu gênero?
# Crie um programa em Python que diga:
# 1 - o número de torcedores por clube
# 2 - a média salarial dos torcedores do Botafogo
# 3 - O número de pessoas moradoras do Rio de Janeiro e torcedoras de outros clubes
# 4 - O número de pessoas de Niterói torcedoras do Fluminense
# 5 - A média de idade das torcedoras femininas do Vasco
# O programa se encerra quando zero for digitado.

print("Pesquisa de Opinião - Times do Coração")
torcedores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
salario_botafogo = 0
idade_vasco_feminino = 0
contador_vasco_feminino = 0
moradores_rj_outros = 0
torcedores_fluminense_niteroi = 0
while True:
    time = int(input("Qual seu time do coração? (1-Flamengo, 2-Vasco, 3-Botafogo, 4-Fluminense, 5-Outros, 0-Sair): "))
    if time == 0:
        break
    if time not in torcedores:
        print("Opção inválida. Tente novamente.")
        continue
    torcedores[time] += 1

    local_moradia = int(input("Onde você mora? (1-Rio de Janeiro, 2-Niterói, 3-Outros): "))
    if local_moradia not in [1, 2, 3]:
        print("Opção inválida. Tente novamente.")
        continue

    salario = float(input("Qual seu salário? "))
    idade = int(input("Qual sua idade? "))
    genero = input("Qual seu gênero? (M/F/O): ").strip().upper()
    if genero not in ['M', 'F', 'O']:
        print("Opção inválida. Tente novamente.")
        continue

    if time == 3:  
        salario_botafogo += salario
    if local_moradia == 1 and time == 5:
        moradores_rj_outros += 1
    if local_moradia == 2 and time == 4:  
        torcedores_fluminense_niteroi += 1
    if genero == 'F' and time == 2: 
        idade_vasco_feminino += idade
        contador_vasco_feminino += 1
print("Número de torcedores por clube:")
print(f"Flamengo: {torcedores[1]}")
print(f"Vasco: {torcedores[2]}")
print(f"Botafogo: {torcedores[3]}")
print(f"Fluminense: {torcedores[4]}")
print(f"Outros: {torcedores[5]}")
if torcedores[3] > 0:
    media_salario_botafogo = salario_botafogo / torcedores[3]
    print(f"Média salarial dos torcedores do Botafogo: R$ {media_salario_botafogo:.2f}")
print(f"Número de moradores do Rio de Janeiro torcedores de outros clubes: {moradores_rj_outros}")
print(f"Número de moradores de Niterói torcedores do Fluminense: {torcedores_fluminense_niteroi}")
if contador_vasco_feminino > 0:
    media_idade_vasco_feminino = idade_vasco_feminino / contador_vasco_feminino
    print(f"Média de idade das torcedoras femininas do Vasco: {media_idade_vasco_feminino:.2f} anos")
else:
    print("Nenhuma torcedora feminina do Vasco foi registrada.")

