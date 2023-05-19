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


