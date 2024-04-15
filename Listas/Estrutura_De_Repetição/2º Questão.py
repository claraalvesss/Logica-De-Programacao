while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario != senha:
        print("Usuário e senha cadastrados com sucesso.")
        break
    else:
        print("Erro: Usuário e senha não podem ser iguais. Tente novamente.")