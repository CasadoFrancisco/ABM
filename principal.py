from BD.conexion import Conexion
import funciones

def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("============= MENU PRINCIPAL =============")
            print("1*- Consultar Profesores")
            print("2*- Consultar Asignaturas")
            print("3*- Consultar Alumnos")
            print("4*- Inscripción de Alumno a Asignatura")
            print("5*- Baja de Alumno de Asignatura")
            print("6*- Modificar")
            print("7*- Salir")
            print("==========================================")
            opcion = int(input("Seleccione una opcion: "))
        
            if opcion < 1 or opcion > 7:
                print("opcion incorrecta, ingrese nuevamente...")
            elif opcion == 7:
                continuar = False
                print("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    conexion = Conexion()

    if opcion == 1:
        try:
            profesores=conexion.listarProfesores()
            
            if len(profesores)>0:
                funciones.listarProfesores(profesores)
                
            else:
                print("no se encontraron profesores")
                
        except :
            print("ocurrio un error....")

    elif opcion == 2:
        try:
            asignaturas=conexion.listarAsignaturas()
            
            if len(asignaturas)>0:
                funciones.listarAsignaturas(asignaturas)
                
            else:
                print("no se encontraron asignaturas disponibles")
                
        except :
            print("ocurrio un error....")
    elif opcion == 3:
        try:
            alumnos = conexion.listarAlumno()

            if len(alumnos)>0:
                funciones.listarAlumno(alumnos)
            else:
                print("no se encontraron alumnos ")
        except:
            print("woooow compadre rompiste todooo")
            
    elif opcion == 4:
        print("ins de alumo a asig")
    elif opcion == 5:
        print("opcion 5")
    elif opcion == 6:
        print("opcion 6")


  
   
menuPrincipal()