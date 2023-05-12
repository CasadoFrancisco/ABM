def listarProfesores(profesores):
    print("profesores:")
    contador=1
    for cur in profesores:
        datos = "{0}.id:{1} | Nombre: {2} | Apellido: {3}"
        print(datos.format(contador, cur[0], cur[1],cur[2]))
        contador= contador+1
    print(" ")

def listarAsignaturas(asignaturas):
    print("Asignaturas:")
    contador =1 
    for cur in asignaturas:
        datos = "{0}. id:{1} | Materia: {2} | turno: {3}"
        print(datos.format(contador,cur[0], cur[1], cur[2], cur[3]))
        contador = contador + 1
    print(" ")

def listarAlumno(Alumnos):
    print("Alumnos")
    contador = 1
    for cur in Alumnos:
        datos = "{0}. id: {1} | Nombre: {2} | Apellido: {3}"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")