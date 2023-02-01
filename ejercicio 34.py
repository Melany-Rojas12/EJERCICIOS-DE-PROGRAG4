# ejercicio34
#Nombre: Melany Rojas
imprimir ( "Inicio del programa" )
def  esYearLeap ( a ñ o ):
    si  un ñ o < 1582 :
        volver  falso
    elif  a ñ o % 400 != 0 :
        volver  falso
    elif  a ñ o % 4 != 0 :
        volver  falso
    elif  a ñ o % 100 != 0 :
        volver  verdadero
    más :
        volver  verdadero
datos de prueba = [ 1900 , 2000 , 2016 , 1987 ]
resultados de la prueba = [ Falso , Verdadero , Verdadero , Falso ]
para  i  en el  rango ( len ( testData )):
    año = datos de prueba [ i ]
    imprimir ( año , '->' , fin = '' )
    resultado = esYearLeap ( año )
    si  resultado == resultados de la prueba [ i ]:
        imprimir ( 'OK' )
    más :
        imprimir ( 'Error' )
print ( "Final del programa" )