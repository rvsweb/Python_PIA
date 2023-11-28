class CuentaBancaria:

    # Atributo privado
    _numero_cuenta = 123456789

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad


# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria(100)

# **Error:** No se puede acceder al atributo _numero_cuenta desde fuera de la clase
print(cuenta._numero_cuenta)
