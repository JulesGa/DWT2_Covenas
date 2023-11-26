class Alumno:
    def __init__(self, nombre, apellido, edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._nota = self.validar_nota(nota)  # Utilizamos un atributo privado para la nota
        self.nacionalidad = nacionalidad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Nota: {self._nota}")
        print(f"Nacionalidad: {self.nacionalidad}")

    def leerNota(self):
        return self._nota

    def registrarNota(self, notaAlumno):
        self._nota = self.validar_nota(notaAlumno)

    def validar_nota(self, nota):
        try:
            nota = float(nota)
            if 0 <= nota <= 20:
                return nota
            else:
                print("La nota debe estar en el rango de 0 a 20.")
                return self._nota  # Mantenemos la nota anterior si la nueva no es válida
        except ValueError:
            print("Ingrese una nota válida.")
            return self._nota
