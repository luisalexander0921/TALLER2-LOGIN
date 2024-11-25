from models.animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    def hace(self):
        return "Ladra"
