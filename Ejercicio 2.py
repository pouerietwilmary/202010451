# 2 Crear un programa que pida al usuario ingresar un número del 0 al 9 y muestre en pantalla el número en letra. 

def volver ():
  num_a_letras()
def num_a_letras():
  definicion = int(input('Introduzca un numero entre 0 y 9: '))

  if definicion == 0:
    print ('CERO')
    volver()
  if definicion == 1:
    print('UNO')
    volver()
  if definicion == 2:
    print('DOS')
    volver()
  if definicion == 3:
    print('TRES')
    volver()
  if definicion == 4:
    print('CUATRO')
    volver()
  if definicion == 5:
    print('CINCO')
    volver()
  if definicion == 6:
    print('SEIS')
    volver()
  if definicion == 7:
    print('SIETE')
    volver()
  if definicion == 8:
    print('OCHO')
    volver()
  if definicion == 9:
    print('NUEVE')
    volver()
  else:
    if definicion != 0 and definicion > 9 :
      print('Su numero es menor que 0 o mayor que 9')
      volver()
