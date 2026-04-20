import sqlite3
import os

class Cliente:
    def __init__(self, namedb = "main.db"):
        self.dbname = namedb
        self.crear_tabla() #Damos la orden inicial de llamar su propio metoo (por eso el self) para que cree la tabla de una
    
    def conectar(self):
        return sqlite3.connect(self.dbname) #Conectamos db
    
    def crear_tabla(self):
        conexion = self.conectar() #Llamamos a nuestro propio metodo (po el self) y hacemos el tunel (la conexion)
        cursor = conexion.cursor() #ponemos conexion ya que es el camino por donde viajaran, y cursor sera la vagoneta
        #cursor es un metodo propio de python para conectar cualquie db, sqlite, mysql, o en la nube

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT,
                Apellido_paterno TEXT,
                Apellido_materno TEXT,
                Telefono TEXT,
                Direccion TEXT,
                RFC TEXT UNIQUE,
                Nacimiento TEXT
            )
        ''')#Creamos la tabla con su estructura sql, id que se autoincrementa, rfc unico
        conexion.commit()#guardamos los datos
        conexion.close()#Cerramos la conexion

    def crear_cliente(self, nombre, apaterno, amaterno, telefono, direccion, rfc, nacimiento):
        self.nombre = nombre
    
