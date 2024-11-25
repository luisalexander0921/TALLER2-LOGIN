class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def hace(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "especie": self.especie,
            "hace": self.hace()
        }
