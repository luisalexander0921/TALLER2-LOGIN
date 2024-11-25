from models.animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Gato")
        self.raza = raza

    def hace(self):
        return "Maulla"
