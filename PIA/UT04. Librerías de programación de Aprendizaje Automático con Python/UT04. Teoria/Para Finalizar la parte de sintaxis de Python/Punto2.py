# CREAR CLASE
# CREAR CONSTRUCTOR POR DEFECTO
# CREAR CONSTRUCTOR PARAMETRIZADO
# CREAR METODO & PROCEDIMIENTO
# CREAR CREAR OBJETOS

# Importar libreria
import math as m

# Crear la clase


class Punto2:

    # Constructor por defecto
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    # Constructor parametrizado
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

# Procedimiento set - Establece los valores
    def distancia(self, point: object) -> float:
        '''Devuelve la distancia entre ambos puntos.'''
        dx = self.x - point.x
        dy = self.y - point.y
        return m.sqrt((dx * dy + dy * dy))

# Metodo get - Devuelve la distancia
    def mostrar(self) -> str:
        return str(self.x) + " : " + str(self.y)


# Crear 1 objeto desde un constructor() por defecto
punto1 = Punto2()
print(punto1.mostrar())

# Crear 2 objeto desde un constructor() parametrizado
punto2 = Punto2(10, 20)
punto2.mostrar()
distancia = punto1.distancia(punto2)
print(distancia)
print(punto1.distancia(punto2))
print(punto1.mostrar())
