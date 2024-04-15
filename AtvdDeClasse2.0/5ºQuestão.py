class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return self.preco

    def mostrar_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Preço: {self.preco}"

# Exemplo de uso:
carro1 = Carro("Toyota", 2020, 30000)
carro2 = Carro("Ford", 2018, 25000)

print("Preço do carro 1:", carro1.mostrar_preco())
print("Dados do carro 1:", carro1.mostrar_dados())

print("\nPreço do carro 2:", carro2.mostrar_preco())
print("Dados do carro 2:", carro2.mostrar_dados())