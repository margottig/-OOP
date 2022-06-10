class CoopEquipo:
    cuentas = []

    def __init__(self, numeroCuenta, cantidad):
        self.numeroCuenta = numeroCuenta
        self.cantidad = cantidad
        CoopEquipo.cuentas.append(numeroCuenta)