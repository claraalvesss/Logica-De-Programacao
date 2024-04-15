class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        return self.endereco

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

# Exemplo de uso:
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
endereco = input("Digite o endereço da pessoa: ")

pessoa1 = Pessoa(nome, idade, endereco)

print("Endereço atual:", pessoa1.mostrar_endereco())

novo_endereco = input("Digite o novo endereço: ")
pessoa1.alterar_endereco(novo_endereco)

print("Novo endereço:", pessoa1.mostrar_endereco())