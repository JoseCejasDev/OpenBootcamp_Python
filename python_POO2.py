
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre, end=" - ")
        print("Nota: ", self.nota)

    def aprobado(self):
        if self.nota >= 7:
            print(f"{self.nombre} con nota: {self.nota} esta Aprobado")
        else:
            print(f"{self.nombre} con nota: {self.nota} esta Desaprobado")

alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("Pedro", 5)
alumno3 = Alumno("Maria", 6)
alumno4 = Alumno("Luis", 7)

alumno1.imprimir()
alumno2.imprimir()
alumno3.imprimir()
alumno4.imprimir()

alumno1.aprobado()
alumno2.aprobado()
alumno3.aprobado()
alumno4.aprobado()