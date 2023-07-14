class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.nacionalidad = "peruana"
        self._saldo = 0

    def validar_edad(self, edad):
        try:
            edad = int(edad)
        except ValueError:
            raise ValueError("La edad debe ser un número entero")
        return edad

    def solicitar_nombre_edad(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = self.validar_edad(input("Ingrese su edad: "))

    def cumpleaños(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        fecha_registro = datetime.now()
        return fecha_registro.strftime("%Y-%m-%d %H:%M:%S")

    def transferencia(self, otra_persona, monto):
        if self._saldo >= monto:
            self._saldo -= monto
            otra_persona._saldo += monto
            print("Transferencia realizada con éxito")
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print("Saldo actual:", self._saldo)


persona1 = Persona("", 0)
persona2 = Persona("", 0)

persona1.solicitar_nombre_edad()
persona2.solicitar_nombre_edad()

monto_transferencia = 100
persona1.transferencia(persona2, monto_transferencia)

<<<<<<< HEAD

=======
>>>>>>> origin/main
persona1.mostrar_saldo()
persona2.mostrar_saldo()