# Ejercicio 32
#Melany Rojas

imprimir ( "Inicio del programa" )
num1 = 0 #Num1 es numero 1
d1 = 0 # d1 es división
def  esPrimo ( num1 ):
    d1 = 2
    mientras que  d1 < num1 :
        si  num1 % d1 == 0 :
            volver  falso
        d1 += 1
    volver  verdadero
para  i  en el  rango ( 1 , 20 ):
    si  esPrimo ( i + 1 ):
        imprimir ( i + 1 , fin = "" )
imprimir ()
print ( "Final del programa" )