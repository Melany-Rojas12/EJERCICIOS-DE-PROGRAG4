# ejercicio34
#Nombre: Melany Rojas
imprimir ( "Inicio del programa" )
def  esYearLeap ( a � o ):
    si  un � o < 1582 :
        volver  falso
    elif  a � o % 400 != 0 :
        volver  falso
    elif  a � o % 4 != 0 :
        volver  falso
    elif  a � o % 100 != 0 :
        volver  verdadero
    m�s :
        volver  verdadero
datos de prueba = [ 1900 , 2000 , 2016 , 1987 ]
resultados de la prueba = [ Falso , Verdadero , Verdadero , Falso ]
para  i  en el  rango ( len ( testData )):
    a�o = datos de prueba [ i ]
    imprimir ( a�o , '->' , fin = '' )
    resultado = esYearLeap ( a�o )
    si  resultado == resultados de la prueba [ i ]:
        imprimir ( 'OK' )
    m�s :
        imprimir ( 'Error' )
print ( "Final del programa" )