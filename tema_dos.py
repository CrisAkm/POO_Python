#Tema 2: Clases y objetos
#Bueno, como ya sabemos, las entidades se modelan en clases, los atributos con el constructor __init__
#y los metodos con funciones que se llaman a si mismo (self), entonces que son los objetos?
#Bueno, los objetos los creamor a partir de la clase.

#Voy a modelar la clase de cliente y proyecto para que quede mas claro lo de objeto
"""Pero antes, voy a enseñar mi diseño de clases ya hecho:
Entidad; Cliente, Atributos: Nombre, Apellido, Direccion, Numero de telefono

Metodos: Requerir, pensar, enviar foto

Entidad: Proyecto, Atributos: Nombre_Cliente, Tipo, Material, Horas, Dificultad

Metodos: instalar, modificar, crear, diseñar, bueno diseñar no, eso seria de la cotizacion o depende 
el casp

Este diseño presenta un par de errores de diseño, por ejemplo, el metodo del cliente pensar, no es
computacionalmente manejable, ¿Como una computadora pensaria?, lo podriamos remplazar por
aprobar_cotizacion() o solicitar_cambios()

En la entidad proyecto, el atributo del nombre del cliente ya lo tenemos en la entidad cliente, asi
que es redundante, lo que hacemos es solo hacer una relacion de un cliente tiene muchos proyectos

Entonces, las relaciones quedan asi:
1 cliente puede tener muchas * cotizaciones
1 cotizacion aprobada se convierte en un 1 proyecto
un 1 cliente puede tener muchos * proyectos"""

class Cliente:
    def __init__(self, nombre, apellido, direccion, numero_telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.numero = numero_telefono

    def requerir(self):
        print(f"El cliente {self.nombre} requiere una cotizacion")

    def enviar_foto(self):
        print(f"Foto de {self.nombre} recibida")

    def solicitar_cambios(self, donde):
        print(f"{self.nombre} solicito un cambio en {donde}")


Cliente1 = Cliente("Andres", "Perez", "Av 5", "+52456789")  #Aqui, creamos el primer objeto, que es
#el cliente 1, objeto de la clase cliente

Cliente1.requerir()
Cliente1.enviar_foto()
Cliente1.solicitar_cambios("Chapa de la puerta")

class Proyecto:
    def __init__(self, Folio, Tipo, Material, Horas, Dificultad):
        self.folio = Folio
        self.tipo = Tipo
        self.material = Material
        self.horas_invertidas = Horas
        self.dificultad = Dificultad
        self.estado = "Fabricacion"

    def instalar(self):
        print(f"Proyecto con folio: {self.folio} de tipo: {self.tipo} instalandose")
        self.estado = "Instalando"
    
    def modificar(self, donde):
        print(f"Proyecto con folio {self.folio} se modificara en {donde}")

Proyecto1 = Proyecto(123, "Puerta", "P400 c18", 19.5, "Dificil")

Proyecto1.instalar()
Proyecto1.modificar("Color blanco")


#ENCAPSULAMIENTOOOOOOOOOOOO!
"""El encapsulamiento tiene como objetivo proteger el codigo, en si una variable, para que solo se modifique bajo ciertos metodos que nosotros pongamos
o en dado caso una variable no modificable y solo de lectura, con variables normales las podemos modificar de la siguiente manera A = 3, protegiendo
la variable self.__A ya no podemos solamente decir __A = 3, nos dara error o nos creara una variable literalmente llamada asi (cuando encapsulamenos la
variable se le cambia el nombre a uno secreto para protegerla), pero no se modificara la original, esto es util cuando tenemos una variable sennsible o
utilizaremos el codigo como libreria"""

class ElectricCar:
    def __init__(self, modelo, tipo, pais):
        self.modelo = modelo
        self.tipo = tipo
        self.pais = pais
        sensor_battery = 0.65 #Simulamos datos del sensor
        self.__battery = sensor_battery  #Variable battery protegida

    def n_pais(self, nuevo_pais):  #ERRORES DE INDENTACIOOON, HABIAS PUESTO
            last_country = self.pais
            self.pais = nuevo_pais #LOS METODOS EN LA DECLARACION DE VARIABLES
            print(f"Datos acuatlizados de {last_country} a {nuevo_pais}")

    def consultar_battery(self):
         #print(self.__battery) #Podriamos agregar este codigo para visualizar el dato nosotros, pero de ninguna manera para sustituir el return
         # ya que tienen dos objetivos diferentes, mientras que el print solo hace visible el valor y se evapora enseguida la variable, el return
         #nos guarda el valor para ser utilizado en codigo si es necesario
        return self.__battery #Este es un getter, lo que hace es que guardamos la variable y su valor para ser utilizado si es necesario


    def calibrar_bateria(self, porcentaje):
        nivel_anterior = self.__battery
        if porcentaje > 0.35 or porcentaje < -0.35:
                print("Valores extremos, remplaza la bateria o el sensor")

        else:
            self.__battery += porcentaje
            print(f"Nivel de bateria de {nivel_anterior} actualizado a {self.__battery}")


car1 = ElectricCar("123A", "Hibrido", "USA")

car1.n_pais("Mexico")

car1.calibrar_bateria(0.35)

car1.__battery = 2
print(car1.__battery)
#Pues, al parecer si imprime 2, pero no es que este modificando la variiable en si,
#Mas bien, esta creando una nueva variable llamada "__battery"

# Imprime todos los atributos que viven en el objeto
print(car1.__dict__) #Esto comprueba lo que digo

print(car1.consultar_battery())