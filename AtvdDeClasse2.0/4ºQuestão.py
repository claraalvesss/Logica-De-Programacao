class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos += segundos
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def diferenca_horarios(self, outro_horario):
        segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        diferenca_segundos = abs(segundos_atual - segundos_outro)
        hora_dif = diferenca_segundos // 3600
        minuto_dif = (diferenca_segundos % 3600) // 60
        segundo_dif = diferenca_segundos % 60
        return hora_dif, minuto_dif, segundo_dif

# Exemplo de uso:
hora1 = Horario(10, 30, 45)
hora2 = Horario(12, 15, 30)

print("Horário 1:", hora1.hora, "h", hora1.minuto, "min", hora1.segundo, "s")
print("Horário 2:", hora2.hora, "h", hora2.minuto, "min", hora2.segundo, "s")

hora1.incrementar_segundos(500)
print("\nHorário 1 após incrementar 500 segundos:", hora1.hora, "h", hora1.minuto, "min", hora1.segundo, "s")

hora2.incrementar_segundos(200)
print("Horário 2 após incrementar 200 segundos:", hora2.hora, "h", hora2.minuto, "min", hora2.segundo, "s")

diferenca = hora1.diferenca_horarios(hora2)
print("\nDiferença entre os horários:", diferenca[0], "h", diferenca[1], "min", diferenca[2], "s")
