from models.animal import Animal

class BoaConstrictor(Animal):
    def __init__(self, nombre, edad, longitud):
        super().__init__(nombre, edad, "Boa Constrictor")
        self.longitud = longitud

    def hace(self):
        return "¡Tsss!"
