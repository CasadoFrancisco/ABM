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
        
               
    
    

    