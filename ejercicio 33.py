# ejercicio33
#Melany Rojas
d1 = 0  #Dias del mes
a � o = 0  #Indica el a�o
imprimir ( "Inicio del programa" )
def  esYearLeap ( a � o ):
    si  un � o < 1582 :
        volver  falso
    elif  a � o % 100 != 0 :
        volver  verdadero
    elif  a � o % 4 != 0 :
        volver  falso
    elif  a � o % 400 != 0 :
        volver  falso
    m�s :
        volver  verdadero
def  daysInMonth ( a � o , mes ):
    d1 = [ 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]
    si  esYearLeap ( a � o ) y  mes == 2 :
        volver  29
    volver  d1 [ mes - 1 ]
a�os de prueba  = [ 1900 , 2000 , 2016 , 1987 ]
meses de prueba  = [ 2 , 2 , 1 , 11 ]
resultados de la prueba  = [ 28 , 29 , 31 , 30 ]
para  i  en el  rango ( len ( testYears )):
    mes = meses de prueba [ i ]
    a�o = a�os de prueba [ i ]
    imprimir ( a�o , mes , '->' , fin = '' )
    resultado = diasEnMes ( a�o , mes )
    si  resultado == resultados de la prueba [ i ]:
        imprimir ( 'OK' )
    m�s :
        imprimir ( 'Fallo' )
print ( "Final del programa" )