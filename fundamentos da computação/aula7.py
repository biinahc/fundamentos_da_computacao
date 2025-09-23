import numpy as np

m = np.ones ((3,3))
contador = 1

print(m)

#Criar uma matriz 3x3 com valores específicos
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("Matriz 3x3:\n", matriz1)

#criar uma matriz 2x4 preenchida com zeros
matriz2 = np.zeros((2,4))
print("\nMatriz 2x4 de zeros:\n", matriz2)

#criar uma matriz 3x3 preenchida com uns
matriz3 = np.ones ((3, 3))
print("\nMatriz 3x3 de uns:\n", matriz3)

#exemplo1
matriz11 = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])

print("Elemento [1][2]:", matriz11[1][2]) #vem 60
print("Primeira Linha:", matriz11[0, :]) #vem 10 20 30 
print("Segunda coluna:", matriz11[:,1]) #vem 20 50 80
print("Submatriz 2x2:\n", matriz11[0:2, 1:3]) #vem 20 30 50 60


#soma
matriz4 = np.array([[1,2],[3,4]])
matriz5 = np.array([[4,0],[5,5]])

print(matriz4+matriz5)
print(np.sum(matriz4))
 

#multiplicação
matriz6 = np.array([[1,2],[3,4]])
matriz7 = np.array([[4,0],[5,5]])

print(matriz6*matriz7)
print(np.dot(matriz6, matriz7))

#soma
matriz8 = np.array([[1,2],[3,4]])
matriz9 = np.array([[4,0],[5,5]])

print(np.sum(matriz8,0))



#exercicio1
#Peça ao usuario para digitar a quantidade de caixas enviadas de 3
#depositos para 3 lojas (matriz 3x3). Depois peça os custos unitários
#por caixa para cada rota (outra matriz 3x3)
#calcule: a) custo por rota; b) custo por deposito; c) custo por loja e d) custo total

quantidade = np.zeros((3,3), dtype=float)
for i in range(3):
    for j in range(3):
        quantidade[i][j] = float(input(f"Digite a quantidade de caixas do depósito {i+1} para a Loka {j+1}:"))
custo_unit = np.zeros((3,3), dtype=float)
for i in range(3):
    for j in range(3):
        custo_unit[i][j] = float(input(f"Digite o custo unitário da rota depoósito {i+1} -> loja {j+1}:"))
custo_por_rota = quantidade * custo_unit
custo_por_deposito = np.sum(custo_por_rota, axis=1)
custo_por_loja = np.sum(custo_por_rota, axis=0)
custo_total = np.sum(custo_por_rota)

print ("")