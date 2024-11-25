from models.animal import Animal

class Hurón(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Hurón")

    def hace(self):
        return "¡Eek Eek!"
