
class Persona:

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def establecer_edad(self, nueva_edad):
        self.edad = nueva_edad

    persona1 = Persona("Juan", 30)

    print(persona1.nombre)
    # print(persona1.obtener_nombre())
    # persona1.establecer_edad(35)
    print(persona1.edad)
