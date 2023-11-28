
class Complex:

    def __init__(self, realpart, imagpart) -> None:
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
x.r, x.i

print(x.r)
print(x.i)
