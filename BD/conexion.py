import mysql.connector
from mysql.connector import Error

class Conexion:
    _instance = None
    

    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = super().__new__(cls)
                cls._instance.conexion = mysql.connector.connect(
                    host="ivar1.toservers.com",
                    port=3306,
                    user="francas",
                    password="U32O8b3H8H",
                    database="francas_universidad"
                )
            except mysql.connector.Error as error:
                print(error)    
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        return cls._instance
    
    #================================================================================= conexion
    


    def listarProfesores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM profesores")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))


    def listarAsignaturas(self):
     if self.conexion.is_connected(): 
         try:
             cursor = self.conexion.cursor()
             cursor.execute("SELECT * FROM asignaturas")  
             resultados = cursor.fetchall()
             return resultados
         except Error as ex:
             print("Error al intentar conexion: {0}".format(ex))

    
    def listarAlumno(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM alumno")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

#----------------------------------------------------------------------------------------------------------#


    def registrarAlumno (self, alumno):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO alumno (id, nombre, apellido) VALUES ({0}, '{1}', '{2}')".format(alumno[0],alumno[1], alumno[2]))
                self.conexion.commit()
                print("Alumno registrado! ")
            except Error as ex:
                print("Error al intentar conexion : {0}".format(ex))



    def registrarProfesores(self, profesor ):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO profesores (id, nombre, apellido) VALUES ({0}, '{1}', '{2}')".format(profesor[0], profesor[1], profesor[2]))
                self.conexion.commit()
                print("profesor registrado !")
              
            except Error as ex:
                print("Error al intentar conexion : {0}".format(ex))  
                



    def registrarAsignaturas(self, asignatura):
         if self.conexion.is_connected():
             print(asignatura)
             try:
                 cursor = self.conexion.cursor()
                 cursor.execute("INSERT INTO asignaturas (id, nombre, turno, id_profesor) VALUES ({0}, '{1}', '{2}', NULL)".format(asignatura[0], asignatura[1], asignatura[2]))

                 
                 self.conexion.commit()
                 print("asignatura creada!")
             except Error as ex :
                 print("Error al crear asignatura: {0}".format(ex))  
                       
#================================================================================    
   

    def asignarAsignaturaProfesor(self, id_profesor, id_asignatura):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
    
                # Verificar si la asignatura ya tiene asignado un profesor
                cursor.execute("SELECT id_profesor FROM asignaturas WHERE id = %s", (id_asignatura,))
                resultado = cursor.fetchone()
    
                if resultado:
                    asignatura_id_profesor_actual = resultado[0]
    
                    if asignatura_id_profesor_actual is not None:
                        # La asignatura ya tiene asignado un profesor, preguntar si se desea reasignar
                        respuesta = input("La asignatura ya tiene asignado un profesor. ¿Desea reasignarla? (S/N): ")
    
                        if respuesta.lower() != "s":
                            print("No se realizó la reasignación de la asignatura.")
                            return
    
                # Actualizar la asignatura con el nuevo profesor
                cursor.execute("UPDATE asignaturas SET id_profesor = %s WHERE id = %s", (id_profesor, id_asignatura))
                self.conexion.commit()
    
                if cursor.rowcount > 0:
                    print("Asignatura asignada al profesor correctamente.")
    
                    # Obtener detalles del profesor y asignatura asignados
                    cursor.execute("SELECT asignaturas.id, asignaturas.nombre, profesores.nombre, profesores.apellido FROM asignaturas LEFT JOIN profesores ON asignaturas.id_profesor = profesores.id WHERE asignaturas.id = %s", (id_asignatura,))
                    resultado = cursor.fetchone()
    
                    if resultado:
                        asignatura_id = resultado[0]
                        asignatura_nombre = resultado[1]
                        profesor_nombre = resultado[2]
                        profesor_apellido = resultado[3]
    
                        print("Asignatura:", asignatura_nombre)
                        print("Profesor asignado:", profesor_nombre, profesor_apellido)
                    else:
                        print("No se encontró la asignatura con ID:", id_asignatura)
                else:
                    print("No se pudo asignar la asignatura al profesor.")
    
            except Error as ex:
                print("Error al asignar asignatura al profesor: {0}".format(ex))


    def registrarInscripcionAlumno(self, id_alumno, id_asignatura):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO alumno_asignatura (id_alumno, id_asignatura) VALUES (%s, %s)", (id_alumno, id_asignatura))
                self.conexion.commit()
                print("Inscripción realizada correctamente.")
            except Error as ex:
                print("Error al realizar la inscripción: {0}".format(ex))

#========================================================


    def buscar_alumno_por_id(self, id_alumno):

      if self.conexion.is_connected():  
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM alumno WHERE id = %s", (id_alumno,))
                alumno = cursor.fetchone()
                return alumno
            except mysql.connector.Error as error:
                print("Error al buscar alumno por ID:", error)
            return None


    
    def eliminar_alumno(self, id_alumno):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM alumno WHERE id = %s", (id_alumno,))
                self.conexion.commit()
                print("Alumno eliminado correctamente.")
            except mysql.connector.Error as error:
                print("Error al eliminar alumno: {0}".format(error))
        else:
            print("No hay conexión a la base de datos.")


    def eliminarAsignaturasPorAlumno(self, id_alumno):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM alumno_asignatura WHERE id_alumno = %s", (id_alumno,))
            self.conexion.commit()
        except mysql.connector.Error as error:
            print("Error al eliminar asignaturas por alumno:", error)




    def buscarProfesorPorId(self, id_profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM profesores WHERE id = %s", (id_profesor,))
                profesor = cursor.fetchone()
                return profesor
            except mysql.connector.Error as error:
                print("Error al buscar el profesor: {0}".format(error))
        else:
            print("No hay conexión a la base de datos.")
            return None

    def eliminar_profesor(self, id_profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM profesores WHERE id = %s", (id_profesor,))
                self.conexion.commit()
                print("Profesor eliminado correctamente.")
            except mysql.connector.Error as error:
                print("Error al eliminar profesor: {0}".format(error))
        else:
            print("No hay conexión a la base de datos.")

   
    def eliminarAsignaturasPorProfesor(self, id_profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM asignaturas WHERE id_profesor = %s", (id_profesor,))
                self.conexion.commit()
                print("Asignaturas eliminadas correctamente.")
            except mysql.connector.Error as error:
                print("Error al eliminar las asignaturas del profesor: {0}".format(error))
        else:
            print("No hay conexión a la base de datos.")



    def eliminarAsignatura(self, id_asignatura):
        if self.conexion.is_connected():
            try:
                cursor =self.conexion.cursor()
                cursor.execute("DELETE FROM asignaturas WHERE id = %s", (id_asignatura,))
                self.conexion.commit()
                print("Asignatura eliminada correctamente.")
            except mysql.connector.Error as error:
                print("Error al eliminar la asignatura: {0}".format(error))
        else:
            print("No hay conexión a la base de datos.")

    def buscarAsignaturaPorId(self, id_asignatura):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM asignaturas WHERE id = %s", (id_asignatura,))
                asignatura = cursor.fetchone()
                return asignatura
            except mysql.connector.Error as error:
                print("Error al buscar la asignatura: {0}".format(error))
        else:
            print("No hay conexión a la base de datos.")
            return None


