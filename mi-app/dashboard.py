import sqlite3
import datetime


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

#AL PARECER, SON METODOS INICIADORES PARA CUALQUIER OPERACION EN DB

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT,
                Apellido_paterno TEXT,
                Apellido_materno TEXT,
                Telefono TEXT,
                Direccion TEXT,
                RFC TEXT UNIQUE,
                Nacimiento TEXT,
                CreacionExp TEXT
            )
        ''')#Creamos la tabla con su estructura sql, id que se autoincrementa, rfc unico
        conexion.commit()#guardamos los datos
        conexion.close()#Cerramos la conexion

    def crear_cliente(self, nombre, apaterno, amaterno, telefono, direccion, rfc, nacimiento):
        conexion = self.conectar()
        cursor = conexion.cursor()
        hoy = datetime.datetime.now()
        #Iniciadores de comunicacion

        try:
            cursor.execute('''
                INSERT INTO Clientes (Nombre, Apellido_paterno, Apellido_materno, Telefono, Direccion, RFC, Nacimiento, CreacionExp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre, apaterno, amaterno, telefono, direccion, rfc, nacimiento, hoy))#? para ingreso de datos seguro

            conexion.commit()
            print(f"Cliente {nombre} registrado exitosamente.")

        except sqlite3.IntegrityError:
            print("error: RFC existente, ingrese otro dato.")

        finally:
            conexion.close()


    def leer_cliente(self, termino_busqueda):
        conexion = self.conectar()
        cursor = conexion.cursor()
        #Iniciadores de comunicacion

        filtro = f"%{termino_busqueda}%" #% es para que busque ese termino sin necesidad de terminar de completar la frase
        #Al parecer, si solo lo pones al principio busca el termino al final, por lo que el signo debe estar tanto al principio
        #Como al final para que funcione la busqueda


        cursor.execute('''
            SELECT * FROM Clientes
            WHERE Nombre LIKE ? OR RFC LIKE ?
            LIMIT 30
        ''', (filtro, filtro)) 
        #Limitamos la devolucion a este codigo a solo el termino que estamos buscando, para evitar devolver
        #toda la tabla, el filtrado lo hacemos desde aca en vez del frontend, y mas importante en sql que es mas rapido
        #Idea de optimizacion mia
        registros = cursor.fetchall()

        conexion.close()
        return registros    
    
    def modificar_cliente(self, quien, donde):
        conexion = self.conectar()
        cursor = conexion.cursor()

        #Aplicaremos un protocolo de seguridad, 
        

mainCliente = Cliente()
mainCliente.crear_cliente("Jna T", "fs", "carmona", "928389", "Av reforma", "9485", "15/15/15")

print(mainCliente.leer_cliente(""))