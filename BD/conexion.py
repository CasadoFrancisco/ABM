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


#creando el alta del profesor a mysql
def crearProfesor(self, nombre, apellido, asignatura):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            # Generamos un ID único para el profesor
            cursor.execute("SELECT MAX(id_profesor) FROM profesor")
            max_id = cursor.fetchone()[0]
            if max_id is None:
                id_profesor = 1
            else:
                id_profesor = max_id + 1
            # Insertamos los datos del profesor en la tabla correspondiente
            sql = "INSERT INTO profesor (id_profesor, nombre, apellido, asignatura) VALUES (%s, %s, %s, %s)"
            val = (id_profesor, nombre, apellido, asignatura)
            cursor.execute(sql, val)
            self.conexion.commit()
            print("Profesor creado exitosamente")
        except Error as ex:
            self.conexion.rollback()
            print(f"Error al intentar crear el profesor: {0}".format(ex))
