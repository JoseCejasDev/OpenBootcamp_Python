#Función que pueda decirte si un número (número entero) es primo o no.
def esPrimo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

print(esPrimo(921))


#Función que devuelve una lista de números primos hasta el número indicado.
def listaPrimos(num):
    lista = []
    for i in range(1, num):
        if esPrimo(i):
            lista.append(i)
    return lista

primos = listaPrimos(1000)
print(primos)