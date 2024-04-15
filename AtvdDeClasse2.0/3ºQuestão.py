class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3


def coletar_dados_alunos():
    alunos = []
    for i in range(5):
        matricula = input("Digite a matrícula do aluno {}: ".format(i+1))
        nome = input("Digite o nome do aluno {}: ".format(i+1))
        nota1 = float(input("Digite a nota da primeira prova do aluno {}: ".format(i+1)))
        nota2 = float(input("Digite a nota da segunda prova do aluno {}: ".format(i+1)))
        nota3 = float(input("Digite a nota da terceira prova do aluno {}: ".format(i+1)))
        alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))
    return alunos


def encontrar_maior_media(alunos):
    maior_media = 0
    aluno_maior_media = None
    for aluno in alunos:
        media = aluno.calcular_media()
        if media > maior_media:
            maior_media = media
            aluno_maior_media = aluno
    return aluno_maior_media

def encontrar_menor_media(alunos):
    menor_media = float('inf')
    aluno_menor_media = None
    for aluno in alunos:
        media = aluno.calcular_media()
        if media < menor_media:
            menor_media = media
            aluno_menor_media = aluno
    return aluno_menor_media

def verificar_aprovacao(aluno):
    media = aluno.calcular_media()
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

alunos = coletar_dados_alunos()

aluno_maior_media = encontrar_maior_media(alunos)
print("Aluno com maior média geral:", aluno_maior_media.nome, "- Média:", aluno_maior_media.calcular_media())

aluno_menor_media = encontrar_menor_media(alunos)
print("Aluno com menor média geral:", aluno_menor_media.nome, "- Média:", aluno_menor_media.calcular_media())

print("\nSituação de cada aluno:")
for aluno in alunos:
    situacao = verificar_aprovacao(aluno)
    print(aluno.nome, "-", situacao)