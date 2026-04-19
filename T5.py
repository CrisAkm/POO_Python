#Pequeño script para manejo de archivos
print("Bienvenido a tu inventario de herramienta")




class Taller:
    def __init__(self, nombre):
        self.nombre = nombre

    def add_tool(self):

        newtool = input("Ingresa tu nueva herramienta aqui: ")

        """Usamos a de append en vez de write, asi evitamos cargar todo en la memoria, lo que haciamos en nuestro anterior
        codigo era leer todo y cargarlo en memoria ram, en la ram agregabamos el siguiente dato, y cuando escribiamos con w, borrabamos
        toda la bdd pero como estaba en ram, se volvia a escribir junto con el nuevo dato, asi que aqui no se cargan los datos a ram
        solo se escribe, asi podemos ahorrar recursos"""
        with open ("bdd.txt", "a") as bdd:
            bdd.write(f"Herramienta agregada: {newtool} \n")
            print(f"La herramienta {newtool} ha sido agregada correctamente")


    def read_tool(self):
        try:
            print("Leyendo toda la base de datos")

            with open ("bdd.txt", "r") as bdd:
                print(bdd.read())
        except FileNotFoundError:
            print("No hay datos existentes.")

NameT = input("Bienvenido, ingresa el nombre de tu taller: ")

def main_app():

    T1 = Taller(NameT) #Anteriormente estaba dentro del while, pero lo sacamos para no estar creando objetos en ciclo
    while True:   
        

        try:
            Selection = int(input(f"Presiona 1 para agregar herramienta \nPresiona 2 para leer los datos \nPresiona 3 para salir\n"))
        except ValueError:
            print("Ingresa solo numeros :)")
            continue

        if Selection == 1:
            T1.add_tool()

        elif Selection == 2:
            T1.read_tool()

        elif Selection == 3:
            print("Nos vemos pronto..")
            break

        else:
            print("Opcion no valida")
            continue

main_app()

#Pues, al parecer ya termine el curso, asi que hare un proyecto con flask despues con permanencia de archivos en json
#para tener mas practicidad y facilidad, es todo por hoy domingo 19 de abril a las 12:27am, termine el curso oficialmente
#(Segun gemini) pero seguire explorando la programacion orientada a objetos para un SaaS que tengo en mente, chao