from BD.conexion import Conexion

def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("============= MENU PRINCIPAL =============")
            print("1*- Alta de Profesor")
            print("2*- Alta de Asignatura")
            print("3*- Alta de Alumno")
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
        print("yaa")
    elif opcion == 2:
        print("alta asign")
    elif opcion == 3:
        print("alta alum")
    elif opcion == 4:
        print("ins de alumo a asig")
    elif opcion == 5:
        print("opcion 5")
    elif opcion == 6:
        print("opcion 6")


  
   
menuPrincipal()