# ejercicio 35
# Nombre:Melany Rojas
imprimir ( "Inicio del programa" )
def  esYearLeap ( a � o ):
    si  un � o < 1582 :
        volver  falso
    elif  a � o % 4 != 0 :
        volver  falso
    elif  a � o % 400 != 0 :
        volver  falso
    elif  a � o % 100 != 0 :
        volver  verdadero
    m�s :
        volver  verdadero
def  daysInMonth ( a � o , mes ):
    mesD�as = [ 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]
    si  esYearLeap ( a � o ) y  mes == 2 :
        volver  29
    volver  mesesD�as [ mes - 1 ]
def  dayOfYear ( a � o , mes , dia ):
    si  un � o < 1582 :
        volver  Ninguno
    si  mes > 12  o  mes < 1 :
        volver  Ninguno
    si  dia > diasEnMes ( a � o , mes ) o  dia < 1 :
        volver  Ninguno
    diastotales = dia
    mes = mes - 1
    mientras  mes > 0 :
        diastotales += diasEnMes ( a � o , mes )
        mes -= 1
    retorno  diastotales
imprimir ( d�aDelA�o ( 2000 , 12 , 31 ))
print ( "Final del programa" )