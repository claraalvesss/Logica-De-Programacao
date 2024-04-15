class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if self.bucho:
            print(f"Conteúdo do bucho de {self.nome}: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está com o bucho vazio.")

    def digerir(self):
        self.bucho = []

macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

macaco1.comer("Banana")
macaco2.comer("Maçã")
macaco1.comer("Pêssego")
macaco2.comer("Pão")

macaco1.ver_bucho()
macaco2.ver_bucho()

macaco1.digerir()
macaco2.digerir()
macaco1.ver_bucho()
macaco2.ver_bucho()
macaco1.comer("Macaco 2")

macaco1.ver_bucho()
macaco1.digerir()
macaco1.ver_bucho()