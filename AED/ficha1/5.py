tempo= float(input("indique o tempo em segundos"))
horas= int(tempo/3600)
tempo= horas*3600
minutos=int(tempo/60)
tempo=minutos*60

print("{0},horas, {1}, minutos, {2} segundos".format(horas,minutos,tempo))


