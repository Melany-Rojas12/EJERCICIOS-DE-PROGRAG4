#ejercicio 40
imprimir ( "Inicio del programa" )
cantidad = int ( input ( "Dimensi�n del vector: " ))
alcalde = 0
menor = 0
yo = 1
desde el  tiempo de  importaci�n del  sue�o
lista = []
importar  al azar
mientras que ( cantidad  >  0 ):
    n�mero = aleatorio . randint ( 50 , 100 )
    lista _ agregar ( n�mero )
    dormir ( 1 )
    yo = 1 + 1
    cantidad = cantidad - 1
    imprimir ( lista )
alcalde = max ( lista )
menor = min ( lista )
para  i  en  rango ( len ( lista ) - 1 ):
    para  j  en  rango ( len ( lista ) - 1 ):
        print ( "El valor de la posicion es: " , lista [ j ], "con" , lista [ j + 1 ])
        si  lista [ j ] > lista [ j + 1 ]:
            temporal = lista [ j ]
            lista [ j ] = lista [ j + 1 ]
            lista [ j + 1 ] = temporal
            print ( "Intercambiando posiciones de: " , lista [ j ], "por" , lista [ j + 1 ])
imprimir ( lista )
dormir ( 1 )
print ( "Final del programa" )
