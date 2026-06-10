# Definición de la clase que representa un objeto del mundo real
class CuentaBancaria:
    # Constructor con 3 atributos requeridos
    def __init__(self, titular, numero_cuenta, saldo_inicial):
        self.titular = titular                # Atributo 1
        self.numero_cuenta = numero_cuenta    # Atributo 2
        self.saldo = saldo_inicial            # Atributo 3

    # Método 1: Depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de ${monto}. Nuevo saldo de {self.titular}: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor a cero.")

    # Método 2: Mostrar la información de la cuenta
    def mostrar_informacion(self):
        print("\n--- Información de la Cuenta ---")
        print(f"Titular: {self.titular}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Saldo Actual: ${self.saldo}")
        print("--------------------------------")

# --- Creación de objetos (Instanciación) ---

# Creación del Objeto 1
cuenta1 = CuentaBancaria("Carlos Pérez", "123456789", 500.0)

# Creación del Objeto 2
cuenta2 = CuentaBancaria("María López", "987654321", 1200.50)

# --- Evidencia de funcionamiento (Uso de los métodos) ---

# Operaciones con la Cuenta 1
cuenta1.mostrar_informacion()
cuenta1.depositar(150.0)
cuenta1.mostrar_informacion()

# Operaciones con la Cuenta 2
cuenta2.mostrar_informacion()
cuenta2.depositar(300.0)