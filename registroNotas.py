import pickle
from alumnos import Alumno

# Función para cargar los datos almacenados
def cargar_datos():
    try:
        with open('alumnos_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Función para guardar los datos
def guardar_datos(alumnos):
    with open('alumnos_data.pkl', 'wb') as file:
        pickle.dump(alumnos, file)

# Función principal
def main():
    print("Bienvenidos al registro de notas")

    alumnos = cargar_datos()

    while True:
        comando = input("Ingrese comando (R para registrar, C para calificar, P para promedio, S para suma, X para salir): ").upper()

        if comando == 'R':
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            edad = int(input("Ingrese la edad del alumno: "))
            nacionalidad = input("Ingrese la nacionalidad del alumno: ")

            nuevo_alumno = Alumno(nombre, apellido, edad, 0, nacionalidad)
            alumnos.append(nuevo_alumno)
            print(f"Alumno {nombre} {apellido} registrado exitosamente.")

        elif comando == 'C':
            for alumno in alumnos:
                nota_valida = False
                while not nota_valida:
                    try:
                        nota = float(input(f"Alumno {alumno.nombre} {alumno.apellido}, Ingrese nota: "))
                        if 0 <= nota <= 20:
                            alumno.registrarNota(nota)
                            nota_valida = True
                        else:
                            print("La nota debe estar en el rango de 0 a 20.")
                    except ValueError:
                        print("Ingrese un número válido para la nota.")

            print("Registro de notas completado.")

        elif comando == 'P':
            if len(alumnos) > 0:
                promedio_notas = sum(alumno.leerNota() for alumno in alumnos) / len(alumnos)
                print(f"El promedio de notas para {len(alumnos)} alumnos es: {promedio_notas:.2f}")
            else:
                print("No hay alumnos registrados.")

        elif comando == 'S':
            suma_notas = sum(alumno.leerNota() for alumno in alumnos)
            print(f"La suma de notas de {len(alumnos)} alumnos es: {suma_notas}")

        elif comando == 'X':
            guardar_datos(alumnos)
            print("Programa finalizado.")
            break

        else:
            print("Comando no reconocido. Intente nuevamente.")

if __name__ == "__main__":
    main()
