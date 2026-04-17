class Trabajador:
    def __init__(self, nombre, sexo, rfc, edad):
        self.nombre = nombre
        self.sexo = sexo
        self.rfc = rfc
        self.edad = edad

    def trabajar(self):
        print(f"El trabajador {self.nombre} ha empezado su jornada.")

class Carpintero(Trabajador): #HERENCIAAAAAAAAAA
    def __init__(self, nombre, sexo, rfc, edad, tipo_madera): #Volvemos a poner los atributos de la clase madre + uno propio
        super().__init__(nombre, sexo, rfc, edad) #Enlazamos los atributos iniciados aca pero pertenecientes a la clase madre
        self.tipo_madera = tipo_madera #Atributo propio

    def lijar(self):
        print(f"El carpintero {self.nombre} esta lijando {self.tipo_madera}")


class Chofer(Trabajador):
    def __init__(self, nombre, sexo, rfc, edad, auto):
        super().__init__(nombre, sexo, rfc, edad)
        self.auto = auto

    def conducir(self):
        print(f"El chofer {self.nombre} ha empezado a conducir en su {self.auto}")


UberLuis = Chofer("Luis", "H", 9090, 34, "Atos")
UberLuis.trabajar()
UberLuis.conducir()

DonGero = Carpintero("Gero", "H", 9898, 45, "Roble de sangre")
DonGero.trabajar()
DonGero.lijar()