base = float(input("Digite o número para calcularmos a potência: "))
expoente = int(input("Digite o expoente para calcularmos a potência: "))

resultado = 1
for _ in range(expoente):
    resultado *= base

print("{} elevado a {} é igual a {}".format(base, expoente, resultado))