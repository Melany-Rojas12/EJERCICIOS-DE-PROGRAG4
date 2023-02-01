# Ejericio 51
print('Inicio del programa')
def validar(nombre, edad, cedula, email):
    if '@' in email:
        if str(nombre):
            for cedula in range(1, 10):
                if edad>0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
print(validar('Melany Rojas', 18, 1754308375, 'mrojasg@est.ups.edu.ec'))
print('Fin del programa')