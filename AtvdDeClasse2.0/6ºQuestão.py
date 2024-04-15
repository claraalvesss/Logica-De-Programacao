class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor

tamagushi = Tamagushi("Tammy", 5, 8, 2)

print("Nome:", tamagushi.retornar_nome())
print("Fome:", tamagushi.retornar_fome())
print("Saúde:", tamagushi.retornar_saude())
print("Idade:", tamagushi.retornar_idade())
print("Humor:", tamagushi.retornar_humor())

tamagushi.alterar_fome(3)
tamagushi.alterar_saude(6)

print("\nApós alterar fome para 3 e saúde para 6:")
print("Fome:", tamagushi.retornar_fome())
print("Saúde:", tamagushi.retornar_saude())
print("Novo humor:", tamagushi.retornar_humor())