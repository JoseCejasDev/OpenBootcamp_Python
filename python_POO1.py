class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Puertas: {self.puertas}"

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}"
 
coche1 = Coche("Rojo", 4, 5, 100, 1600)
print(coche1)