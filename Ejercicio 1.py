# 1 Crear un programa que pida números positivos al usuario, y vaya calculandola suma de todos ellos (terminará cuando se teclea un número negativo o cero).

np  =  int ( input ( 'Ingrese un numero' ))
sumatotal  = []
sumatotal.append ( np )
while  np  >  0:
  np  =  int ( input ( 'Ingrese un numero a sumar' ))
  sumatotal.append(np)

if  np  <=  0 :
  print (sumatotal)
  print (sum(sumatotal))
