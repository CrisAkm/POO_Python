from abc import ABC, abstractmethod
#TEMA 4: POLIMORFISMOOOOOOOOOOO, hare un sencillo codigo para calcular nominas como parte de esta practica

class Empleado(ABC):
    def __init__(self, nombre, rfc, sexo):
        self.nombre = nombre
        self.rfc = rfc
        self.sexo = sexo
        self.salariob = 1800


    def nomina(self, multiplicador, horasx, comisiones):
        if multiplicador < 1:
            print("no puede ser el salario menor al minimo.")
            multiplicador = 1

        salario_hora = (self.salariob * multiplicador)/ 48
        if horasx < 0:
            print("Error logico, revisa tus horas extras ingresadas.")
            horasagregar = 0
        elif horasx == 0:
            horasagregar = 0            
        elif horasx <= 9:
            horasagregar = salario_hora * 2 * horasx
        elif horasx > 9:
            horasagregar = salario_hora * 3 * horasx
            print("Advertencia: Riesgo ante la LFT")
        
        

        nominafinal = (self.salariob * multiplicador) + horasagregar + comisiones
        print(f"El salario de {self.nombre} es de ${nominafinal}")
        return nominafinal
    
    @abstractmethod
    def iniciar_jordana (self):
        pass
    
class Herrero(Empleado):
    def __init__(self, nombre, rfc, sexo, epp):
        super().__init__(nombre, rfc, sexo)
        self.epp = epp

    def iniciar_jordana(self):
        print(f"el herrero {self.nombre} esta trabajando protegido con {self.epp}")

class Vendedor(Empleado):
    def __init__(self, nombre, rfc, sexo, totalvendido):
        super().__init__(nombre, rfc, sexo)
        self.totalvendido= totalvendido


    def iniciar_jordana(self):
        print(f"El vendedor {self.nombre} ha iniciado su jornada y ha vendido: ${self.totalvendido}")

class Gerente(Empleado):
    def __init__(self, nombre, rfc, sexo, zona):
        super().__init__(nombre, rfc, sexo)
        self.zona = zona

    def iniciar_jordana(self):
        print(f"El gerente de la zona {self.zona} ha llegado.")

Luis = Vendedor("Luis", 900, "H", 1000)
Luis.nomina(1, 90, 100)

Marco = Herrero("Marco", 900, "H", "Lentes y tapones")
Marco.nomina(1.5, 9, 0)

Teresa = Gerente("Teresa", 4090, "M", "Tlaxcala")
Teresa.nomina(5, 0, 1000)




    
