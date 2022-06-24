import time

hora = int(time.strftime('%H'))
minutos = int(time.strftime('%M'))

if hora >= 19:
	print ("Ya es la hora de irse a casa") 
else:
	print (f"Quedan {18-hora} horas y {59-minutos} minutos de trabajo")