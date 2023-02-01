# ejercicio 35
# Nombre:Melany Rojas
imprimir ( "Inicio del programa" )
def  esYearLeap ( a ñ o ):
    si  un ñ o < 1582 :
        volver  falso
    elif  a ñ o % 4 != 0 :
        volver  falso
    elif  a ñ o % 400 != 0 :
        volver  falso
    elif  a ñ o % 100 != 0 :
        volver  verdadero
    más :
        volver  verdadero
def  daysInMonth ( a ñ o , mes ):
    mesDías = [ 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]
    si  esYearLeap ( a ñ o ) y  mes == 2 :
        volver  29
    volver  mesesDías [ mes - 1 ]
def  dayOfYear ( a ñ o , mes , dia ):
    si  un ñ o < 1582 :
        volver  Ninguno
    si  mes > 12  o  mes < 1 :
        volver  Ninguno
    si  dia > diasEnMes ( a ñ o , mes ) o  dia < 1 :
        volver  Ninguno
    diastotales = dia
    mes = mes - 1
    mientras  mes > 0 :
        diastotales += diasEnMes ( a ñ o , mes )
        mes -= 1
    retorno  diastotales
imprimir ( díaDelAño ( 2000 , 12 , 31 ))
print ( "Final del programa" )