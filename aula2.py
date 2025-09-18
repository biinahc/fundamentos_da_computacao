#atividade1
#elabore um programa que receba como entrada a base e altura de um retangulo, calcule e mostre sua área.

#resolução:
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
print("A área do retângulo é:", area)


#atividade2

#Elabore um programa que receba a idade de uma pessoa como entrada e calcule quantos meses, dias e horas a pessoa possui.

#resolução:
idade_anos = int(input("Digite sua idade em anos: "))
idade_meses = idade_anos * 12  
idade_dias = idade_anos * 365
idade_horas = idade_dias * 24
print(f"Sua idade em meses é: {idade_meses} meses")
print(f"Sua idade em dias é: {idade_dias} dias")
print(f"Sua idade em horas é: {idade_horas} horas")

#atividade3
#Elabore um programa que receba a temperatura em Celsius e exiba em Kelvin e Fahrenheit.
#resolução:
celsius = float(input("Digite a temperatura em Celsius: "))
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Kelvin é: {kelvin} K")
print(f"A temperatura em Fahrenheit é: {fahrenheit} °F")

#ATIVIDADE 3
#Um sistema de ponto eletrônico registra as horas trabalhadas em formato decimal (ex: 7.75 horas). Crie um programa que leia esse valor e converta para o formato HH horas e MM minutos.

#RESOLUÇÃO:
horas_trabalhadas = float(input("Digite as horas trabalhadas em formato decimal (ex: 7.75): "))
horas = int(horas_trabalhadas)
minutos = int((horas_trabalhadas - horas) * 60)
print(f"Você trabalhou {horas} horas e {minutos} minutos.")

#ATIVIDADE 4
# Elabore um programa onde o usuário informa um horário no formato
# hh:mm (24h) e um tempo adicional em minutos. O programa deve calcular e
# exibir o horário resultante, também no formato hh:mm. Você deve
# considerar: A soma pode ultrapassar 24h, então o horário deve “girar o
# relógio”.
#RESOLUÇÃO:
horario = input("Digite o horário no formato hh:mm (24h): ")
tempo_adicional = int(input("Digite o tempo adicional em minutos: "))
horas, minutos = map(int, horario.split(":"))
total_minutos = horas * 60 + minutos + tempo_adicional
total_minutos = total_minutos % (24 * 60)
horas_resultante = total_minutos // 60
minutos_resultante = total_minutos % 60
print(f"O horário resultante é: {horas_resultante:02}:{minutos_resultante:02}")

#ATIVIDADE 5
# Elabore um programa que recebe dois números e verifica se eles são iguais.
#RESOLUÇÃO:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 == num2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")

#ATIVIDADE 6
# Elabore um programa que peça ao usuário três valores numéricos e
# compare se o primeiro é maior que o segundo, e o segundo maior que o
# terceiro.

#RESOLUÇÃO:
valor1 = float(input("Digite o primeiro valor numérico: "))
valor2 = float(input("Digite o segundo valor numérico: ")) 
valor3 = float(input("Digite o terceiro valor numérico: "))
if valor1 > valor2 and valor2 > valor3:
    print("O primeiro valor é maior que o segundo, e o segundo é maior que o terceiro.")

else:
    print("A condição não é satisfeita.")   
#ATIVIDADE 7
# Elabore um programa que receba base e altura de dois terrenos. Calcule as áreas e verifique se o primeiro terreno é maior que o segundo.

#RESOLUÇÃO:
base1 = float(input("Digite a base do primeiro terreno: "))
altura1 = float(input("Digite a altura do primeiro terreno: "))
area1 = base1 * altura1
base2 = float(input("Digite a base do segundo terreno: "))
altura2 = float(input("Digite a altura do segundo terreno: "))
area2 = base2 * altura2
resultado = area1 > area2
print(f"O primeiro terreno é maior que o segundo: {resultado}")

#ATIVIDADE 8
# Elabore um programa que receba três notas, calcule a média ponderada e verifique se a nota é maior ou igual a 6.

#RESOLUÇÃO:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
print(f"A média ponderada é: {media_ponderada}")

if media_ponderada >= 6:
    print("A média é maior ou igual a 6.") 
else:
    print("A média é menor que 6.")

#ATIVIDADE 9
# Elabore um programa que receba o valor original e o valor atual de um
# produto. Calcule a diferença percentual entre os valores e verifique se a
# variação é maior que 20% para mais ou para menos.
#RESOLUÇÃO:
valor_original = float(input("Digite o valor original do produto: "))
valor_atual = float(input("Digite o valor atual do produto: "))
diferenca_percentual = ((valor_atual - valor_original) / valor_original) * 100
print(f"A diferença percentual é: {diferenca_percentual:.2f}%")
if abs(diferenca_percentual) > 20:
    print("A variação é maior que 20%.")    
else:
    print("A variação não é maior que 20%.")

#ATIVIDADE 10
# Elabore um programa para calcular se uma casa ultrapassou o limite permitido de
# consumo de energia por cômodo. O sistema deve receber como entrada:
# - O número total de cômodos (int)
# - O consumo médio por cômodo em kWh (float)
# - O limite máximo de consumo total permitido (const, 500.0 kWh)
# Com base nas entradas, calcule:
# - O consumo total.
# - Se o consumo total excedeu o limite (retorne True ou False).
# - Se a média por cômodo é maior que 75 kWh e o total ultrapassa o limite.
# Exiba todos os resultados.

#RESOLUÇÃO:
num_comodos = int(input("Digite o número total de cômodos: "))
consumo_medio = float(input("Digite o consumo médio por cômodo em kWh: "))
limite_maximo = 500.0
consumo_total = num_comodos * consumo_medio
excedeu_limite = consumo_total > limite_maximo
media_maior_75_e_excedeu = consumo_medio > 75 and excedeu_limite
print(f"O consumo total é: {consumo_total} kWh")
print(f"O consumo total excedeu o limite: {excedeu_limite}")
print(f"A média por cômodo é maior que 75 kWh e o total ultrapassa o limite: {media_maior_75_e_excedeu}")

#ATIVIDADE 11
# Um satélite coleta dados sobre a temperatura de uma região em três horários
# distintos do dia. Escreva um programa em Python que receba três valores de
# temperatura (em graus Celsius), calcule a média aritmética das temperaturas

# e:

# - Verifique se a média está acima de 40°C ou se alguma das temperaturas
# individuais ultrapassou 50°C.
# - Calcule a diferença entre a maior e a menor temperatura.
# Mostre no final:

# - A média das temperaturas.
# - A diferença entre a maior e a menor.
# - Um aviso (True/False) indicando se há risco de superaquecimento, de
# acordo com a regra do item 1.
# Dica: use max(), min() e operadores lógicos.

#RESOLUÇÃO:
temp1 = float(input("Digite a primeira temperatura em °C: "))
temp2 = float(input("Digite a segunda temperatura em °C: "))
temp3 = float(input("Digite a terceira temperatura em °C: "))
media_temperaturas = (temp1 + temp2 + temp3) / 3
risco_superaquecimento = media_temperaturas > 40 or temp1 > 50 or temp2 > 50 or temp3 > 50
diferenca_temp = max(temp1, temp2, temp3) - min(temp1, temp2, temp3)
print(f"A média das temperaturas é: {media_temperaturas:.2f} °C")
print(f"A diferença entre a maior e a menor temperatura é: {diferenca_temp:.2f} °C")
print(f"Risco de superaquecimento: {risco_superaquecimento}")

