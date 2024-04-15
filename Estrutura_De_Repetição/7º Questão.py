inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

numeros_no_intervalo = list(range(inicio, fim + 1))
soma_intervalo = sum(numeros_no_intervalo)

print("Números no intervalo:", numeros_no_intervalo)
print("Soma dos números no intervalo:", soma_intervalo)