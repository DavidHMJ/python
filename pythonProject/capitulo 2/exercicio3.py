print ("tempo do primeiro trecho")
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTempo = 15

#print(" Tempo do primeiro trecho em segundos: ", totalTempoPrimeiroTrecho)

print("Tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundoSegundotrecho = 12 * 3
# print("Tempo do segundo trecho em segundos: ", totalTempoSegundoTrecho)

print ("tempo do terceiro trecho: 8 min e 15 s")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTempo = 15
#print(" Tempo do terceiro trecho em segundos: ", totalTempoTerceiroTrecho)
# soma o total de minumetros e converte todos os minutos em segundos

totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

# soma valor total dos segundos
totalTempoTodosTrechosSegundos = (segundoPrimeiroTempo + segundoSegundotrecho + segundoTerceiroTempo)

restantesMinutos = int(totalTempoTodosTrechosSegundos / 60)
restantesSegundos = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMinutos + restantesMinutos
totalSegundos = restantesSegundos

print("soma de tempo de todos os trechos: ", totalMinutos, "Minutos")
print("Soma de tempo de todos os trechos: ", totalSegundos, "segundos")

horaInicialSegundos  = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horarioInicialSegundos = horaInicialSegundos + minutoInicialSegundos

tempoTrechoMinutosSegundos = totalMinutos * 60

horaChegada = int(((horarioInicialSegundos + tempoTrechoMinutosSegundos) / 60) / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutosSegundos) / 60) % 60)
print(" O tempo de chegada foi de " , horaChegada, ":", minutoChegada, restantesSegundos)