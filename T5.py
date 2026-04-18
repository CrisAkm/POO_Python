#Pequeño script para manejo de archivos
print("Bienvenido a tu inventario de herramienta")

newtool = input("Ingresa tu nueva herramienta aqui")

"""Usamos a de append en vez de write, asi evitamos cargar todo en la memoria, lo que haciamos en nuestro anterior
codigo era leer todo y cargarlo en memoria ram, en la ram agregabamos el siguiente dato, y cuando escribiamos con w, borrabamos
toda la bdd pero como estaba en ram, se volvia a escribir junto con el nuevo dato, asi que aqui no se cargan los datos a ram
solo se escribe, asi podemos ahorrar recursos"""
with open ("bdd.txt", "a") as bdd:
    bdd.write(f"Nueva herramienta agregada: {newtool} \n")


class Taller:
    def __init__(self, nombre):
        self.nombre = nombre

    def add_tool(self, herramienta):
        pass