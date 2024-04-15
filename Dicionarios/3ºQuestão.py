notas = {}
media = 0

for i in range(4):
    nota = float(input("Insira a {}° nota: ".format(i + 1)))
    media = media + nota
    notas[f"Nota {i + 1}"] = nota

print("Notas dos alunos:\n", notas)
print("A média das notas é:", media / 4)