class Aluno:
    def __init__(self, nome, numero_matricula, curso):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.curso = curso

    def mostrar_curso(self):
        return self.curso

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso

# Exemplo de uso:
nome = input("Digite o nome do aluno: ")
numero_matricula = input("Digite o número de matrícula do aluno: ")
curso = input("Digite o curso do aluno: ")

aluno1 = Aluno(nome, numero_matricula, curso)

print("Curso atual:", aluno1.mostrar_curso())

novo_curso = input("Digite o novo curso: ")
aluno1.alterar_curso(novo_curso)

print("Novo curso:", aluno1.mostrar_curso())
