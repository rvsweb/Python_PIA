import math as m


class Punto:

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def mostrar(self):
        return str(self.x) + ":" + str(self.y)

    def distancia(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return m.sqrt((dx * dy + dy * dy))
