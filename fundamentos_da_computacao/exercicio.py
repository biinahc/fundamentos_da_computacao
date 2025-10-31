notas = []
for i in range(4):
    aluno = [float(input(f"Aluno {i+1}, nota {d}: ")) for d in ["Matemática", "Português", "Ciências"]]
    notas.append(aluno)

print("\nMédia de cada aluno:")
for i, aluno in enumerate(notas):
    print(f"Aluno {i+1}: {sum(aluno)/3:.2f}")

print("\nMédia de cada disciplina:")
for j in range(3):
    media = sum(notas[i][j] for i in range(4)) / 4
    print(f"{['Matemática', 'Português', 'Ciências'][j]}: {media:.2f}")