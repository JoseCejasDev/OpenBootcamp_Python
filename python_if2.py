numero_inicial = 2
numero_final = 8
lista_impares = []

while numero_inicial <= numero_final:
    if numero_inicial % 2 != 0:
        lista_impares.append(numero_inicial)
    numero_inicial += 1

print(lista_impares)