from BD.conexion import Conexion


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
    print("Alumnos: ")
    contador = 1
    for cur in Alumnos:
        datos = "{0}. id: {1} | Nombre: {2} | Apellido: {3}"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")



#----------------------------------------------------------------------



def registrarAsignatura():
    idCorrecto = False

    while not idCorrecto:
        id = input("Ingrese ID (4 digitos):")

        if id.isnumeric() and len(id) == 4:
            idCorrecto = True
            id = int(id)
        else:
            print("El ID debe ser un numero de 4 digitos, Ingrese nuevamente")
    nombre = input("Ingrese Nombre de materia: ")
    turno = input("Ingrese turno: (ma;ana o tarde )")
    
    asignatura = (id, nombre, turno)
    return asignatura
    

def registrarProfesores():
     idCorrecto = False
     while not idCorrecto:
         id = input("Ingrese ID (6 dígitos): ")
         if id.isnumeric() and len(id) == 6:
             idCorrecto = True
             id = int(id)
         else:
             print("El ID debe ser un número de 6 dígitos. Ingrese nuevamente.")
     nombre = input("Ingrese Nombre: ")
     apellido = input("Ingrese Apellido: ")
     profesor = (id, nombre, apellido)
     return profesor


def registrarAlumno():
    idCorrecto = False
    while not idCorrecto:
        id = input("Ingrese ID (6 dígitos): ")
        if id.isnumeric() and len(id) == 6:
            idCorrecto = True
            id = int(id)
        else:
             print("El ID debe ser un número de 6 dígitos. Ingrese nuevamente.")
    nombre = input("ingese Nombre: ")
    apellido = input("ingrese Apellido: ")
    alumno = (id, nombre, apellido)
    return alumno

#============================================================

def mostrar_asignaturas_disponibles():
    conexion = Conexion()
    asignaturas = conexion.listarAsignaturas()
    if asignaturas:
        print("Asignaturas disponibles:")
        for asignatura in asignaturas:
            print("ID: {0} - Nombre: {1} - Turno: {2}".format(asignatura[0], asignatura[1], asignatura[2]))

def registrar_inscripcion_alumno(id_alumno, id_asignatura):
    conexion = Conexion()
    conexion.registrarInscripcionAlumno(id_alumno, id_asignatura)


def eliminar_alumno(conexion, id_alumno):
    alumno = conexion.buscar_alumno_por_id(id_alumno)
    if alumno:
        confirmacion = input("¿Está seguro que desea eliminar el alumno? (s/n): ")
        if confirmacion.lower() == "s":
            # Eliminar asignaturas asociadas al alumno
            conexion.eliminar_asignaturas_por_alumno(id_alumno)
            
            # Eliminar al alumno
            conexion.eliminar_alumno(id_alumno)
            
            print("Alumno eliminado correctamente.")
    else:
        print("No se encontró un alumno con el ID especificado.")




def eliminar_profesor(conexion, id_profesor):
    profesor = conexion.buscarProfesorPorId(id_profesor)
    if profesor:
        confirmacion = input("¿Está seguro que desea eliminar al profesor? (s/n): ")
        if confirmacion.lower() == "s":
            # Eliminar asignaturas asociadas al profesor
            conexion.eliminarAsignaturasPorProfesor(id_profesor)
            
            # Eliminar al profesor
            conexion.eliminar_profesor(id_profesor)
            
            print("Profesor eliminado correctamente.")
    else:
        print("No se encontró un profesor con el ID especificado.")

    

def eliminarAsignatura(conexion, id_asignatura):
    asignatura = conexion.buscarAsignaturaPorId(id_asignatura)
    if asignatura:
        confirmacion = input("¿Está seguro que desea eliminar la asignatura? (s/n): ")
        if confirmacion.lower() == "s":
            # Eliminar asignatura de los profesores
            conexion.eliminarAsignaturasPorProfesor(id_asignatura)

            # Eliminar asignatura de los alumnos
            conexion.eliminarAsignaturasPorAlumno(id_asignatura)

            # Eliminar la asignatura
            conexion.eliminarAsignatura(id_asignatura)

            print("Asignatura eliminada correctamente.")
    else:
        print("No se encontró una asignatura con el ID especificado.")






