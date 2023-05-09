from BD.conexion import Conexion

def menuPricipal():
    continuar = True
    while(continuar):
       opcionCorrecta = False
       while(not opcionCorrecta):
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
        
            if opcion < 1 | opcion > 7:
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
    print("============ ALTA DE PROFESOR ============")
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    asignatura = input("Ingrese la asignatura del profesor: ")
    conexion.crearProfesor(nombre, apellido, asignatura)


menuPricipal()