import json
import os

bdd_cliente = "bdd_cliente.json"

class Cliente:
    def __init__(self, id, nombre, apaterno, amaterno, telefono, direccion, rfc, nacimiento):
        self.id = id
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.telefono = telefono
        self.direccion = direccion
        self.rfc = rfc
        self.nacimiento = nacimiento

    def readc(self):
        if os.path.exists(bdd_cliente):

            with open(bdd_cliente, 'r') as archivo:
                return json.load(archivo)
            
        else:
            return[]
    
    def createc(self):
            
            nuevo_cliente = {
            "ID": self.id,
            "NOMBRE": self.nombre,
            "Apellido_paterno": self.apaterno,
            "Apellido_materno": self.amaterno,  #LLEVAN COMAS, COMAAASS, NO SE TE OLVIDE, DEBES HACER UN SEPARADOR
            "Telefono": self.telefono,
            "direccion": self.direccion,
            "rfc": self.rfc,
            "Fecha de nacimiento": self.nacimiento 
        }
            with open (bdd_cliente, 'a') as archivo:
                json.dump(nuevo_cliente, archivo, indent=4)

            

C1 = Cliente(3, "Luis", "Perez", "Molina", 24111111, "Av reforma", 9000, "01/04/01")

C1.createc()

lol = C1.readc()

print(len())


