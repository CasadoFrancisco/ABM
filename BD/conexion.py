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
   

    def asignarAsignaturaProfesor(self, id_profesor, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("UPDATE asignaturas SET id_profesor = %s WHERE id = %s", (id_profesor, id))
                self.conexion.commit()
                print("Asignatura asignada al profesor correctamente.")
            except Error as ex:
                print("Error al asignar asignatura al profesor: {0}".format(ex))

    


        

