import time 

tempo = time.time()


def tempo_em_horas(tempo):
    minut = tempo // 60
    res = tempo / 60
    segundos = res - minut
    hora = minut // 60
    ris = minut / 60
    minutos = ris - hora
    lista = [hora, minutos, segundos]
    return lista

def tempo_em_dias(tempo):
    lista = tempo_em_horas(tempo)
    dias = lista[0] // 24
    anos = dias // 365
    cal = [dias, anos]
    return cal

temp = tempo_em_dias(tempo)
print(f'A quantidade de dias é {temp[0]}, e de anos é {temp[1]}')
