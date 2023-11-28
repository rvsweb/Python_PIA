class CuentaBancaria:

    # Atributo protegido
    _interes_anual = 0.05

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad


# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria(100)

# **Error:** No se puede acceder al atributo _interes_anual desde fuera de la clase
# print(cuenta._interes_anual)

# **Correcto:** Se puede acceder al atributo _interes_anual desde una subclas


class CuentaAhorro(CuentaBancaria):

    def calcular_intereses(self):
        return self.saldo * self._interes_anual


# Crear un objeto de la clase CuentaAhorro
cuenta_ahorro = CuentaAhorro(100)

# Acceder al atributo _interes_anual desde la subclas
print(cuenta_ahorro._interes_anual)
