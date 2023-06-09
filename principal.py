from BD.conexion import Conexion
import funciones
import os


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            limpiar_consola()
            print("============= MENU PRINCIPAL =============")
            print("1*- Profesores")
            print("2*- Alumnos")
            print("3*- Asignaturas")
            print("4*- Salir")
            print("==========================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 4:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 4:
                continuar = False
                print("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    conexion = Conexion()

    if opcion == 1:
        menuProfesores(conexion)

    elif opcion == 2:
        menuAlumnos(conexion)

    elif opcion == 3:
        menuAsignaturas(conexion)


def menuProfesores(conexion):
    opcionCorrecta = False
    while not opcionCorrecta:
        limpiar_consola()
        print("============= MENU PROFESORES =============")
        print("1*- Listar profesores")
        print("2*- Crear profesor")
        print("3*- Eliminar profesor")
        print("4*- Volver al menú principal")
        print("==========================================")
        opcion = int(input("Seleccione una opción: "))

        if opcion < 1 or opcion > 4:
            print("Opción incorrecta, ingrese nuevamente...")
        elif opcion == 4:
            opcionCorrecta = True
        elif opcion == 1:
            try:
                profesores = conexion.listarProfesores()
                if len(profesores) > 0:
                    funciones.listarProfesores(profesores)
                else:
                    print("No se encontraron profesores registrados.")
                input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Presione Enter para continuar...")
        elif opcion == 2:
            profesor = funciones.registrarProfesores()
            try:
                conexion.registrarProfesores(profesor)
                print("Profesor registrado correctamente.")
                input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error en la inscripción de profesores:", e)
                input("Presione Enter para continuar...")
        elif opcion == 3:
            try:
                profesores = conexion.listarProfesores()
                if len(profesores) > 0:
                    funciones.listarProfesores(profesores)
                    id_profesor = input("Ingrese el ID del profesor: ")
                    funciones.eliminar_profesor(conexion, id_profesor)
                    print("Profesor eliminado correctamente.")
                    input("Presione Enter para continuar...")
                else:
                    print("No se encontraron profesores registrados.")
                    input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Presione Enter para continuar...")


def menuAlumnos(conexion):
    opcionCorrecta = False
    while not opcionCorrecta:
        limpiar_consola()
        print("============= MENU ALUMNOS =============")
        print("1*- Listar alumnos")
        print("2*- Crear alumno")
        print("3*- Eliminar alumno")
        print("4*- Volver al menú principal")
        print("========================================")
        opcion = int(input("Seleccione una opción: "))

        if opcion < 1 or opcion > 4:
            print("Opción incorrecta, ingrese nuevamente...")
        elif opcion == 4:
            opcionCorrecta = True
        elif opcion == 1:
            try:
                alumnos = conexion.listarAlumno()
                if len(alumnos) > 0:
                    funciones.listarAlumno(alumnos)
                else:
                    print("No se encontraron alumnos registrados.")
                input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Presione Enter para continuar...")
        elif opcion == 2:
            alumno = funciones.registrarAlumno()
            try:
                conexion.registrarAlumno(alumno)
                print("Alumno registrado correctamente.")
                input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error en la inscripción de alumnos:", e)
                input("Presione Enter para continuar...")
        elif opcion == 3:
            try:
                alumnos = conexion.listarAlumno()
                if len(alumnos) > 0:
                    funciones.listarAlumno(alumnos)
                    id_alumno = input("Ingrese el ID del alumno: ")
                    funciones.eliminar_alumno(conexion, id_alumno)
                    print("Alumno eliminado correctamente.")
                    input("Presione Enter para continuar...")
                else:
                    print("No se encontraron alumnos registrados.")
                    input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Presione Enter para continuar...")


def menuAsignaturas(conexion):
    opcionCorrecta = False
    while not opcionCorrecta:
        limpiar_consola()
        print("============= MENU ASIGNATURAS =============")
        print("1*- Listar asignaturas")
        print("2*- Crear asignatura")
        print("3*- Eliminar asignatura")
        print("4*- Volver al menú principal")
        print("===========================================")
        opcion = int(input("Seleccione una opción: "))

        if opcion < 1 or opcion > 4:
            print("Opción incorrecta, ingrese nuevamente...")
        elif opcion == 4:
            opcionCorrecta = True
        elif opcion == 1:
            try:
                asignaturas = conexion.listarAsignaturas()
                if len(asignaturas) > 0:
                    funciones.listarAsignaturas(asignaturas)
                else:
                    print("No se encontraron asignaturas registradas.")
                input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Presione Enter para continuar...")
        elif opcion == 2:
            asignatura = funciones.registrarAsignatura()
            try:
                conexion.registrarAsignaturas(asignatura)
                print("Asignatura registrada correctamente.")
                input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error en la inscripción de asignaturas:", e)
                input("Presione Enter para continuar...")
        elif opcion == 3:
            try:
                asignaturas = conexion.listarAsignaturas()
                if len(asignaturas) > 0:
                    funciones.listarAsignaturas(asignaturas)
                    id_asignatura = input("Ingrese el ID de la asignatura: ")
                    funciones.eliminarAsignatura(conexion, id_asignatura)
                    print("Asignatura eliminada correctamente.")
                    input("Presione Enter para continuar...")
                else:
                    print("No se encontraron asignaturas registradas.")
                    input("Presione Enter para continuar...")
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Presione Enter para continuar...")


menuPrincipal()
