mercado = {}

for i in range(3):
    produto = str(input("Insira o nome do {}° produto: ".format(i + 1)))
    preço = float(input("Insira o preço do(a) {}: R$ ".format(produto)))
    mercado[produto] = preço

print("Mercado:\n", mercado)