#calcular el area de un triangulo
def area_triangulo(base,altura):
    return base*altura/2
 
#calcular el area de un circulo
def area_circulo(radio):
    PI = 3.1416
    return PI*radio**2

print(area_triangulo(3,4))
print(area_circulo(10))