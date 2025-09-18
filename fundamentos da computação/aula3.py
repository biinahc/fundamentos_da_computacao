#atividade1

#Elabore um programa para verificar se um número é positivo ou negativo.

#RESOLUÇÃO:
num = float(input("Digite um número: "))
if num >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")

#ATIVIDADE 2

# Elabore um programa para verificar se uma pessoa é maior de idade ou não.
#RESOLUÇÃO:
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#ATIVIDADE 3
# Elabore um programa que receba 3 números e diga o maior entre eles.
#RESOLUÇÃO:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 >= num2 and num1 >= num3:
    print("O maior número é:", num1)
elif num2 >= num1 and num2 >= num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)

#ATIVIDADE 4
# Elabore um programa que receba 3 notas de um aluno e
# indique se ele foi aprovado (média maior ou igual a 7),
# reprovado (média menor que 5) ou está de recuperação.

#RESOLUÇÃO:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em recuperação.")

#ATIVIDADE 5
# Elabore um programa que receba os 3 lados de um triângulo e diga se ele é equilátero, escaleno ou isósceles.

#RESOLUÇÃO:
lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("O triângulo é escaleno.")
else:
    print("O triângulo é isósceles.")   

#ATIVIDADE 6
# Elabore um programa que o usuário digite uma senha e
# verifique se ela é válida seguindo as seguintes regras:
# - Entre 8 a 12 caracteres
# - Contém o caractere @
# - Não começa com números

#RESOLUÇÃO:
senha = input("Digite uma senha: ")
if 8 <= len(senha) <= 12 and "@" in senha and not senha[0].isdigit():
    print("Senha válida.")  
else:
    print("Senha inválida.")

#ATIVIDADE 7
# Elabore um programa em que o usuário digite seu nome,
# idade e código de acesso. Verifique se a pessoa tem idade
# entre 18 e 60 anos, o nome não está vazio, e o código de
# acesso é um número par maior que 100. Imprima se o
# acesso foi validado com sucesso ou não.

#RESOLUÇÃO:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
codigo_acesso = int(input("Digite o código de acesso: "))
if nome and 18 <= idade <= 60 and codigo_acesso > 100 and codigo_acesso % 2 == 0:
    print("Acesso validado com sucesso.")
else:
    print("Acesso não validado.")

#ATIVIDADE 8
# Elabore um programa em python que receba um número e
# imprima a sua raiz quadrada caso ele seja positivo e o
# quadrado do número caso ele seja negativo

#RESOLUÇÃO:
num = float(input("Digite um número: "))
if num >= 0:
    raiz_quadrada = num ** 0.5
    print(f"A raiz quadrada de {num} é {raiz_quadrada}")
else:
    quadrado = num ** 2
    print(f"O quadrado de {num} é {quadrado}")

#ATIVIDADE 9
#Elabore um programa em python que entre com o valor de x e imprima f(x) = 8/2-x

#RESOLUÇÃO:
x = float(input("Digite o valor de x: "))
f = 8 / (2 - x)
print(f"O valor de f(x) é: {f}")

#ATIVIDADE 10
# Você foi contratado por uma pequena loja para desenvolver um sistema simples de gestão de
# estoque de produtos. A loja precisa de um programa que colete dados dos seus produtos e gere
# relatórios baseados em critérios específicos.
# O programa deve permitir o cadastro de 3 produtos, onde é informado pelo usuário.
# Para cada produto, o usuário deve informar:
# Nome do produto (string)
# Quantidade em estoque (inteiro)
# Preço unitário (float)
# Após o cadastro:
# Mostrar o valor total em estoque(R$) de todos os produtos.
# Listar todos os produtos que possuem estoque abaixo de 5 unidades.
# Calcular e mostrar a média de preços dos produtos.
# Mostrar os produtos com preço acima da média e estoque acima de 10 unidades.

#RESOLUÇÃO:
num_produtos = 3

nome1 = input("Digite o nome do produto 1: ")
quantidade1 = int(input("Digite a quantidade em estoque do produto 1: "))
preco1 = float(input("Digite o preço unitário do produto 1: "))

nome2 = input("Digite o nome do produto 2: ")
quantidade2 = int(input("Digite a quantidade em estoque do produto 2: "))
preco2 = float(input("Digite o preço unitário do produto 2: "))

nome3 = input("Digite o nome do produto 3: ")
quantidade3 = int(input("Digite a quantidade em estoque do produto 3: "))
preco3 = float(input("Digite o preço unitário do produto 3: "))

valor_total_estoque = (quantidade1 * preco1) + (quantidade2 * preco2) + (quantidade3 * preco3)
print(f"O valor total em estoque é: R${valor_total_estoque:.2f}")
print("Produtos com estoque abaixo de 5 unidades:")
if quantidade1 < 5:
    print(f"- {nome1} (Estoque: {quantidade1})")
if quantidade2 < 5:
    print(f"- {nome2} (Estoque: {quantidade2})")
if quantidade3 < 5:
    print(f"- {nome3} (Estoque: {quantidade3})")
media_precos = (preco1 + preco2 + preco3) / num_produtos
print(f"A média de preços dos produtos é: R${media_precos:.2f}")
print("Produtos com preço acima da média e estoque acima de 10 unidades:")
if preco1 > media_precos and quantidade1 > 10:
    print(f"- {nome1} (Preço: R${preco1:.2f}, Estoque: {quantidade1})")
if preco2 > media_precos and quantidade2 > 10:
    print(f"- {nome2} (Preço: R${preco2:.2f}, Estoque: {quantidade2})")
if preco3 > media_precos and quantidade3 > 10:
    print(f"- {nome3} (Preço: R${preco3:.2f}, Estoque: {quantidade3})")


#ATIVIDADE 12
# Uma universidade deseja automatizar o processo de análise para concessão de bolsas com base
# em diferentes critérios. Você deve escrever um programa que receba os seguintes dados de um
# estudante: Nome do estudante, Idade (inteiro), Média final no último semestre (float), Renda
# familiar mensal per capita (float), Número de atividades extracurriculares realizadas (inteiro). Com
# base nesses dados, o sistema deve analisar e imprimir a situação do estudante, conforme as
# regras abaixo:

# O estudante só pode ser considerado para bolsa se:
# - A média for maior ou igual a 7.0
# - E a renda per capita for menor que R$ 2.000 ou se ele tiver realizado pelo menos 3 atividades
# extracurriculares

#Resolução:
nome_estudante = input("Digite o nome do estudante: ")
idade = int(input("Digite a idade do estudante: "))
media_final = float(input("Digite a média final do último semestre: "))
renda_per_capita = float(input("Digite a renda familiar mensal per capita: "))
num_atividades = int(input("Digite o número de atividades extracurriculares realizadas: "))

criterio_media = media_final >= 7.0
criterio_renda = renda_per_capita < 2000.0
criterio_atividades = num_atividades >= 3

concede_bolsa = criterio_media and (criterio_renda or criterio_atividades)

if concede_bolsa:
    print(f"O estudante {nome_estudante} está elegível para a bolsa.")
else:
    print(f"O estudante {nome_estudante} não está elegível para a bolsa.")

print("Detalhes da análise:")
print(f"- Média final >= 7.0: {criterio_media}")
print(f"- Renda per capita < R$ 2.000: {criterio_renda}")
print(f"- Atividades extracurriculares >= 3: {criterio_atividades}")
print(f"- Concessão de bolsa: {concede_bolsa}")


