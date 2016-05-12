CONSTRUA uma pagina que mostra a temperatura media de cada dia do mes de marco,
a partir das temperaturas minimas e maximas ocorridas em cada dia.
No final, seu programa deve mostrar a media das temperaturas minimas e
a media de maximas e o percentual de dias atipicos(isto eh, com temperatura
                                                   media menor 15C ou superior a 38C). Faca uma funcao que receba a temperatura
media de um dia e retorne 1 se for atipico ou 0 caso contrario.

atipico / tipico

media(minima / max)

days = []
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_if_not_tipical_day(month):
    for day in month:
        # adiciona um valor entre 10 e 50 para a temperatura media
        med_temp = randint(10, 50)
        # instancia a Variavel atipico como 0 em dias normais
        atipico = 0
        if (med_temp < 15) | (med_temp > 38):
            # caso seja um dia atipico, o marcador atipico mudara e sera
            # adicionado na variavel 'dia'
            atipico = 1
            dia = {'dia': day, 'atipico': atipico}
            media
        else:
            dia = {'dia': day, 'atipico': atipico}
        days.append(dia)
    # retorna o valor dos dias
    return days


def count_atipical_porcentage(days):
    # contador de dias atipicos para fazer a media de dias atipicos
    atipico_count = 0
    for element in days:
        if (days['atipico'] == 1):
            atipico_count += 1
    # calcula a media de dias atipicos
    media = ((atipico_count) / (len(days)))
    return media
