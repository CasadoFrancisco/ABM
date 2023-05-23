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
            print("4*- Inscripcion de Profesores ")
            print("5*- Inscripcion asignatura ")
            print("6*- Inscripcion de alumnos")
            print("7*- Asignar asignatura a profesor")
            print("10*- Salir")
            print("==========================================")
            opcion = int(input("Seleccione una opcion: "))
        
            if opcion < 1 or opcion > 10:
                print("opcion incorrecta, ingrese nuevamente...")
            elif opcion == 10:
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
                
        except Exception as e:
            print("ocurrio un error....",e)



    elif opcion == 2:
        try:
            asignaturas=conexion.listarAsignaturas()
            
            if len(asignaturas)>0:
                funciones.listarAsignaturas(asignaturas)
                
            else:
                print("no se encontraron asignaturas disponibles")
                
        except Exception as e:
            print("ocurrio un error....", e)


    elif opcion == 3:
        try:
            alumnos = conexion.listarAlumno()

            if len(alumnos)>0:
                funciones.listarAlumno(alumnos)
            else:
                print("no se encontraron alumnos ")
        except Exception as e:
            print("woooow compadre rompiste todooo", e)



    elif opcion == 4:
       profesor = funciones.registrarProfesores()
       try:
            conexion.registrarProfesores(profesor)
       except Exception as e:
            print("Ocurrio un error en la inscripcion de profesores...", e)


            
    elif opcion == 5:
        asignatura = funciones.registrarAsignatura()
        try:
            conexion.registrarAsignaturas(asignatura)
        except Exception as e:
            print("ocurrio algo al agregar una asignatura!", e)


    elif opcion == 6:
        alumnos = funciones.registrarAlumno()
        try:
            conexion.registrarAlumno(alumnos)
        except Exception as e:
           print("Ocurrio un error al agregar un alumno!", e)


    elif opcion == 7:
        try:
            profesores = conexion.listarProfesores()
            if len(profesores) > 0:
                funciones.listarProfesores(profesores)
                id_profesor = input("Ingrese el ID del profesor: ")
                asignaturas = conexion.listarAsignaturas()
                if len(asignaturas) > 0:
                    funciones.listarAsignaturas(asignaturas)
                    id_asignatura = input("Ingrese el ID de la asignatura: ")
                    conexion.asignarAsignaturaProfesor(id_profesor, id_asignatura)
                    print("Asignatura asignada al profesor correctamente.")
                else:
                    print("No se encontraron asignaturas.")
            else:
                print("No se encontraron profesores.")
        except Exception as e:
            print("Ocurrió un error:", e)
            
     
     



  
   
menuPrincipal()