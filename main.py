entrada = (int(input("digite quantos minutos quer retornar em horas:  ")))
hora = int(entrada/60)
minutos = int(entrada % 60)
if len(str(minutos)) == 1:
    minutos = '0' + str(minutos)
  #print ("São {} horas e {}".format(hora,minutos)
print('horas -----> ' + str(hora) + ':' + str(minutos))