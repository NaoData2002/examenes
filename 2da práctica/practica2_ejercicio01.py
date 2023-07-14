from datetime import datetime

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.nacionalidad = "peruana"

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

# Crear instancia de la clase Persona
persona = Persona("", 0)

# Solicitar nombre y edad
persona.solicitar_nombre_edad()

# Incrementar edad dos veces usando el método cumpleaños
persona.cumpleaños()
persona.cumpleaños()

# Mostrar edad actualizada
<<<<<<< HEAD

print("Edad actualizada:", persona.edad)

# Obtener fecha y hora de registro

=======
print("Edad actualizada:", persona.edad)

# Obtener fecha y hora de registro
>>>>>>> origin/main
fecha_registro = persona.obtener_fecha_registro()
print("Fecha de registro:", fecha_registro)