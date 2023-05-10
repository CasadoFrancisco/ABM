import mysql.connector
from mysql.connector import Error

class Conexion():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="kevinahumada.com.ar",
                user="kevinahu_franci",
                password="2BhNwieRJdRe",
                database="kevinahu_universidad"
            )
            
        except Error as ex:
            print(f"Error al intentar la conexion: {0}".format(ex))
    
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f"Error al intentar la conexion: {0}".format(ex))


    