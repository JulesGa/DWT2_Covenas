La lógica de la aplicación es la siguiente:

1) “Ingrese comando: “, el programa debe esperar a que el usuario ingrese un comando el
cual debe ser R, C, P, S o X, en donde se tiene lo siguiente:

2) R : Registrar alumnos, el programa deberá preguntar los datos principales de un alumno
(Nombre, Apellido, Edad y Nacionalidad).

3) C : Comando para calificar a los alumnos. Al presionar este comando se debe preguntar
el ingreso de notas para cada uno de los alumnos de la siguiente forma:

(a) Alumno <Nombre Apellido> , Ingrese nota: 15
(b) Alumno <Nombre Apellido> , Ingrese nota: 17
(c) Alumno <Nombre Apellido> , Ingrese nota: 12

4) Validar que las notas ingresadas deban estar en un rango de 0 a 20 y no se debe aceptar
caracteres u otro tipo de dato, solo acepta números. En caso se ingresen datos erróneos se
debe volver a preguntar por la nota del alumno. Al terminar con el registro de notas se
debe volver a preguntar por el ingreso de otro comando. El programa es ciclico.

5) El comando P es un comando que permite obtener el promedio de todos los alumnos
registrados y mostrarlo con el mensaje:

(a) El promedio de notas para <Cantidad de alumnos> es : <Promedio de notas>

6) El comando S se utilizará para desplegar la suma de notas de todos los alumnos
registrados mostrando el siguiente mensaje:

(a) La suma de notas de <Cantidad de alumnos> es: <Suma total de notas>