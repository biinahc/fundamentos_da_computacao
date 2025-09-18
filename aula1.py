#Elabore um programa que identifique se uma string é um palíndromo ou não.

#dicas
#texto = texto.lower() -- Converte para minúsculas para comparação
#texto = texto.replace(" ", "") -- Remove espaços em branco
#texto = texto.replace(" ", "") -- Remove espaços em branco
#inverso = texto[::-1] -- Inverte a string

#resolução

texto = input("Digite uma palavra: ")
texto_limpo = texto.replace(" ", "").lower()
inverso = texto_limpo[::-1]
if texto_limpo == inverso:
    print(f"A palavra '{texto}' é um palíndromo.")
else:
    print(f"A palavra '{texto}' NÃO é um palíndromo.")

#ATIVIDADE 2

# Você recebeu a seguinte string de rastreamento de uma nota fiscal eletrônica:
# registro =
# "NF:BR-2025/09/03-INV-004587|Total=R$12.345,67|Status=APROVADO"

# Extraia a seguintes informações utilizando fatiamento:
# 1 - Extraia o código do país (BR).
# 2 - Pegue a data completa (2025/09/03) e, a partir dela, extraia ano, mês e dia
# separadamente.
# 3 - Extraia o número da nota (INV-004587) e mostre apenas os 3 últimos dígitos.
# 4 - Recupere o valor total (R$12.345,67).
# 5 - Capture o status (APROVADO) e mostre também ele invertido (ODAVORPA).
# 6 - Faça uma “amostragem” da data pegando um caractere a cada 2 posições.

#RESOLUÇÃO

registro = "NF:BR-2025/09/03-INV-004587|Total=R$12.345,67|Status=APROVADO"
codigo_pais = registro[3:5]

data = registro[6:16] 
ano = data[0:4]
mes = data[5:7]
dia = data[8:10]

numero_nota = registro[17:27]
ultimos_digitos = numero_nota[-3:] 
inicio_valor = registro.find("R$")
valor_total = registro[inicio_valor:inicio_valor + 11]

inicio_status = registro.find("Status=") + len("Status=")
status = registro[inicio_status:] 
status_invertido = status[::-1]

amostragem_data = data[::2]  

print("Código do país:", codigo_pais)
print("Data completa:", data)
print("Ano:", ano, "Mês:", mes, "Dia:", dia)
print("Número da nota:", numero_nota)
print("Últimos 3 dígitos:", ultimos_digitos)
print("Valor total:", valor_total)
print("Status:", status)
print("Status invertido:", status_invertido)
print("Amostragem da data:", amostragem_data)


#ATIVIDADE 3

#Elabore um programa que solicite o nome de uma cidade e estado e mostre essa informação.

#RESOLUÇÃO:

cidade = input("Digite o nome da cidade: ")
estado = input("Digite o nome do estado: ")
print(f"Você mora em", cidade + "-" + estado)

#ATIVIDADE 4
# Elabore um programa para que o usuário digite sua idade e mostre o tipo da variável antes e depois da conversão.

idade_str = input("Digite sua idade: ")
print("Antes da conversão:", type(idade_str))

idade_int = int(idade_str)
print("Depois da conversão:", type(idade_int))
print("Sua idade é:", idade_int)

#ATIVIDADE 5

# Elabore um programa que receba o nome e ultimo sobrenome de uma pessoa e crie um e-mail instituicional no formato nome.ultimosobrenome@empresa.com

#RESOLUÇÃO:

nome = input("Digite seu nome completo: ").lower()
partes = nome.split()
email = f"{partes[0]}.{partes[-1]}@empresa.com"
print (partes)
print("Seu e-mail institucional é:", email)

#ATIVIDADE 6

#Elabore um programa onde o usuário digite uma frase com 3 palavras entre colchetes. Imprima apenas essas palavras

frase = input("Digite uma frase com 3 palavras entre colchetes: ")

abertura1 = frase.find("[") + 1
fechamento1 = frase.find("]")

abertura2 = frase.find("[", fechamento1) + 1
fechamento2 = frase.find("]", fechamento1 + 1)

abertura3 = frase.find("[", fechamento2) + 1
fechamento3 = frase.find("]", fechamento2 + 1)

tag1 = frase[abertura1:fechamento1]
tag2 = frase[abertura2:fechamento2]
tag3 = frase[abertura3:fechamento3]
print("Palavras entre colchetes:", tag1 + ", " + tag2 + ", " + tag3)


#ATIVIDADE 7

#elabore um programa que solicite ao usuario as seguintes informações: Nome completo, idade e telefone e exiba as informações formatadas de maneira organizada.

#RESOLUÇÃO:

nome = input("Digite seu nome completo: ")
idade = input("Digite sua idade: ")
telefone = input("Digite seu telefone: ")

telefone_formatado = f"({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}"
print(f"Nome: {nome}\nIdade: {idade}\nTelefone: {telefone_formatado}")



