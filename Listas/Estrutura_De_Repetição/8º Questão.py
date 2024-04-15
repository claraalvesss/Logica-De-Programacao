numero = int(input("Digite um número para gerar a tabuada: "))

print("Tabuada de :",numero)
for i in range(1, 11):
    resultado = numero * i
    print("{} X {} = {}".format(numero, i, resultado))