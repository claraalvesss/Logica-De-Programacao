while True:
    nota = float(input("Digite uma nota entre zero e dez por favor: "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Valor inválido. Tente novamente.")