caixa_misteriosa = {}

for i in range(4):
    item = input(f"Insira o {i + 1}º item na Caixa Misteriosa: ")
    caixa_misteriosa[i + 1] = item

numero = int(input("Digite um número para revelar o que está na Caixa Misteriosa: "))

if 1 <= numero <= len(caixa_misteriosa):
    print(f'O item na posição {numero} é: {caixa_misteriosa[numero]}')
else:
    print("Número inválido.")
