#Función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def mostrarBisiestos(num):
    if esBisiesto(num):
        print(f"{num} es un año bisiesto")
    else:
        print(f"{num} No es un año bisiesto")

anio = int(input("Introduce un año: "))
mostrarBisiestos(anio)