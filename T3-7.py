from abc import ABC, abstractmethod 
#Porque un nuevo archivo? bueno, es que necesitamos importar esta libreria integrada para este tema
#3.7 CLASES Y METODOS ABSTRACTOS

#Basicamente, lo que hacemos es crear una clase y metodos abstractos literalmente xd, solo que de esta clase no podemos
#crear objetos directamente, pero si clases, y los metodos los podemos dejar sin codigo o seguir programando en cada clase hija

class Habitacion(ABC): #Iniciamos la clase abstracta, no podemos crear ningun objeto a partir de esta, la hacemos derivada de ABC
    def __init__(self, prioridad):
        self.prioridad = prioridad

    @abstractmethod # DECORADOOOOR, añade codigo a la funcion por venir, ya sea antes, despues, o antes y despues, pero invisible
    #Necesario para un metodo abstracto
    def servicio(self):
        pass #Cada quien programa su servicio que quiere


class Familiar(Habitacion):
    def __init__(self, prioridad, control_parental):
        super().__init__(prioridad)
        self.cp = control_parental

    def servicio(self):
        if self.cp == True:
            servicio_18 = False
            print("Este es un lugar seguro para todos :D")

        else:
            print("Diviertanse ;)")
            servicio_18 = True
        return servicio_18
    
class VIPDeluxe(Habitacion):
    def __init__(self, prioridad, accesos):
        super().__init__(prioridad)
        self.accesos = accesos

    def servicio(self):
        print("Tienes un asistente privado para lo que necesites")
        asistente_priv = True
        return asistente_priv

BrayanIker = Familiar(3, False)
BrayanIker.servicio()
TonyRV = VIPDeluxe(1, "all")
TonyRV.servicio()
