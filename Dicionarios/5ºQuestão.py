funcionarios = {}

for i in range(3):
    funcionario = input("Digite o nome do funcionário: ")
    funcionarios[f'Funcionário {i + 1}'] = funcionario

print("Funcionários:", funcionarios)

demissao = input("Digite o nome do funcionário a ser demitido: ")

chaves_para_remover = [chave for chave, valor in funcionarios.items() if valor == demissao]

for chave in chaves_para_remover:
    del funcionarios[chave]
    print(f'{demissao} foi demitido.')

if not chaves_para_remover:
    print(f'{demissao} não encontrado na lista de funcionários.')

print("Funcionários restantes:", funcionarios)