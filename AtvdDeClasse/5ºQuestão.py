class Televisor:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 10

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal_atual = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("Número de canal inválido. Deve estar entre 1 e 100.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo.")

    def mostrarStatus(self):
        print(f"Canal: {self.canal_atual}, Volume: {self.volume}")
