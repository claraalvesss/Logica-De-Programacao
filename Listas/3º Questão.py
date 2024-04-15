a = [int(input("Digite o {}º elemento do primeiro vetor: ".format(i + 1))) for i in range(10)]
b = [int(input("Digite o {}º elemento do segundo vetor: ".format(i + 1))) for i in range(10)]

c = [None] * 20

for i in range(10):
    c[2 * i] = a[i]
    c[2 * i + 1] = b[i]

print("\nAgora observe o terceiro vetor intercalado:", c)