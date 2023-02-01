# ejercicio33
#Melany Rojas
d1 = 0  #Dias del mes
a ñ o = 0  #Indica el año
imprimir ( "Inicio del programa" )
def  esYearLeap ( a ñ o ):
    si  un ñ o < 1582 :
        volver  falso
    elif  a ñ o % 100 != 0 :
        volver  verdadero
    elif  a ñ o % 4 != 0 :
        volver  falso
    elif  a ñ o % 400 != 0 :
        volver  falso
    más :
        volver  verdadero
def  daysInMonth ( a ñ o , mes ):
    d1 = [ 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]
    si  esYearLeap ( a ñ o ) y  mes == 2 :
        volver  29
    volver  d1 [ mes - 1 ]
años de prueba  = [ 1900 , 2000 , 2016 , 1987 ]
meses de prueba  = [ 2 , 2 , 1 , 11 ]
resultados de la prueba  = [ 28 , 29 , 31 , 30 ]
para  i  en el  rango ( len ( testYears )):
    mes = meses de prueba [ i ]
    año = años de prueba [ i ]
    imprimir ( año , mes , '->' , fin = '' )
    resultado = diasEnMes ( año , mes )
    si  resultado == resultados de la prueba [ i ]:
        imprimir ( 'OK' )
    más :
        imprimir ( 'Fallo' )
print ( "Final del programa" )