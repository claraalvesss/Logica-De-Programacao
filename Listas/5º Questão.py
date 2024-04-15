idade = [int(input("Insira a idade do {}º aluno: ".format(i + 1))) for i in range(10)]
altura = [float(input("Insira a altura do {}º aluno: ".format(i + 1))) for i in range(10)]

media = sum(altura)/10
quantidade = 0

for i in range(10):
  if idade[i] > 13:
    if altura[i] < media:
      quantidade = quantidade + 1

print("A quantidade de alunos com idade maior que 13 anos e com altura inferior à média da altura são: {}".format(quantidade))