class CuentaBancaria:

    # Atributo público
    saldo = 0

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad


# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria(100)

# Acceder al saldo de la cuenta
print(cuenta.saldo)

# Depositar dinero en la cuenta
cuenta.depositar(100)

# Verificar el saldo de la cuenta
print(cuenta.saldo)

# Retirar dinero de la cuenta
cuenta.retirar(50)

# Verificar el saldo de la cuenta
print(cuenta.saldo)
