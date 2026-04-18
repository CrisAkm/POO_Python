import json #Libreria para gestionar o crear json
import os #Libreria para movernos en el sistema


ARCHIVO_BD = "base_de_datos.json"

def read_db():
    """Lee el archivo JSON si existe, caso contrario devuelve la lista"""
    if os.path.exists(ARCHIVO_BD):
        #r significa read, osea que el sistema verifica que exista base_de_datos.json, y si si existe
        #leemos 
        with open(ARCHIVO_BD, 'r') as archivo:
            return json.load(archivo)
    return []#Returnamos lista vacia en caso de no existir el archivo, MUY IMPORTANTE RETORNAR, si no pues el codigo
    #Se rompe porque basicamente todo funciona en base a una estructura de lista
        #Abrimos de manera segura la base de datos y la guardamos en
        #la variable archivos, open significa abrir, obviamente abrir o acceder a la base de datos
        #with, es un bloque de seguridad, podemos simplemente poner  xd = open(archivo.txt) pero necesitariamos añadir 
        #un xd.close() al final para cerrar el archivo, dejarlo de utiliar, ya que si no lo cerramos, o algo sale mal
        #y nos imposibilita el cerrar el archivo por un bug y queda abierto, los datos se pueden corromper o no poder
        #acceder manualmente al archivo "archivo.txt", entonces el with actua poniendo ese .close() por nosotros
        #en cualquier escenario

#Lista global que servira como base de datos 
tasks = read_db()

def save_db():
    #Guarda la lista global "Task[]" en el JSON
    with open(ARCHIVO_BD, 'w') as archivo: #La w significa write
        json.dump(tasks, archivo, indent=4)
        """dump: verter o volvar. Lo que hace la linea json.dump es llamar a la libreria json que importamos,
        luego la funcion o metodo jump(Tarea que aprendere a diferenciar en POO) que basicamente es un traductor
        de python a json, porque aunque en vsc y en ide se vea legible en realidad es un lenguaje con su
        propia matematica, lo que hace dump es traducir los datos a json y no solo guardar los caractares probablemente
        ilegibles, donde 'tasks' es el que informacion se guardara, 'archivo donde', 'indent=4' el formato
        para hacer mas legible el archivo json por si solo"""



def add_task(name, description, status, time, priority, days):
    #Creamos un diccionario, parecido a un archivo JSON que tiene dato:valordd
    new_task = {
        "NOMBRE": name,
        "DESCRIPCION": description,
        "ESTADO": status,  #LLEVAN COMAS, COMAAASS, NO SE TE OLVIDE, DEBES HACER UN SEPARADOR
        "TIEMPO": time,
        "PRIORIDAD": priority,
        "DIAS": days
    }
    #Agregamos el diccionario a la lista principal
    tasks.append(new_task)
    save_db()
    print(f"Tarea '{name}' agregada correctamente")

#add_task("prueba", "p1", "p2", "p3", "p4", "p5")
#print(tasks) Para ver la base de datos, solo probando

def read_task():
    print("!--Listas de tareas--!")
    if len(tasks) == 0:
        print("No hay tareas pendientes :)")
    else:
        for i in tasks:
           # print(f"NOMBRE: {tasks[name]}, ESTADO: {tasks[status]}") !!mal, intentamos buscar en tasks
           #y no podemos buscar en esa base de datos directamente, pero ya hemis cargado esa misma base en la variable
           #i, entonces hacemos i['NOMBRE'] donde i es la base de datos, nombre la clave que buscamos y nos arrojara
           #el valor
           print(f"Nombre: {i['NOMBRE']}, Estado: {i['ESTADO']}")
           print("\n")

        
def update_task(number_task, feature_update, value):
    tasks[number_task][feature_update] = value
    save_db()
    print("modificacion exitosa")

def delete_task(position):
    tasks.pop(position)
    save_db()
    print(f"Tarea {position+1} eliminada correctamente")

    
    


def main_app():
    while True:
        print("Bienvenido a tu Gestor de Tareas\n " \
        "Selecciona la tarea a realizar: \n" \
        "1 - Agregar nueva tarea. \n" \
        "2 - Leer las tareas \n" \
        "3 - Modificar tarea \n" \
        "4 - Eliminar tarea \n" \
        "5 - Salir")
        try: #Aqui ibamos a meter toda la app, absolutamente toda al try, pero no fue necesario, try puede aislar
            #La linea especifica que puede fallar y salvar todo el proceso, aunque parezca que interrumpe el flujo
            #funciona
            selection = int(input("Ingresa el numero de opcion que realizaras: \n"))#Ponemos int ya que lo toma como str
        except ValueError:
            print("Ingresa datos validos.")
            continue

        if selection == 5:
            print("Hasta luego :)")
            break
        elif selection == 1:
            print("Agregando nueva tarea...")
            try:
                name = input("Nombre de la tarea: ")
                description = input("Agrega una breve descripcion: ")
                status = input("La tarea esta completada? Responde con si o no: ")
                capitalletterstatus = status.upper()
                if capitalletterstatus not in ["SI","NO","SI.","NO."]:
                    print("Solo se aceptan respuestas de si y no, continuemos al inicio \n")
                    continue
                time = float(input("Ingresa los minutos que invertiras en esta tarea: "))
                priority = float(input("Ingresa el nivel de prioridad de la tarea, siendo 1 inmediato y 3 para despues: "))
                if priority < 1 or priority > 3:
                    print("Ingresa los valores correctos. \n")
                    continue

                days = []

                """       def routine():
                    routineday = input("Ingresa el dia que vas a agregar. Ejemplo: Solo hoy, Lunes, Martes, Etc..")
                    routinedaycl = routineday.upper()
                    if routinedaycl not in ["SOLO HOY","LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]:
                        print("Datos no validos.")
                        return 0
                    else:
                        days.append(routinedaycl)"""#Funcionaba bien, pero solo poDIAS agregar un dia mas, y 
                #aparte era una funcion anidada, era una mala practica en python, lo resolvimos con un while
                #dentro de otro en vez de una funcion dentro de un if dentro de un while

                dayst = input("Ingresa los DIAS que se repetiran la tarea\n" \
                "Ejemplo: Solo hoy, Lunes, Martes, Etc.. Solo escribe un dia: ")
                dayst2 = dayst.upper()
                if dayst2 not in ["SOLO HOY","LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO",]:
                    print("Datos no validos.")
                    continue
                days.append(dayst2)
                
                anotherday = input("Deseas agregar otro dia? Si o no:")
                anotherdaycapitalletter = anotherday.upper()
                if anotherdaycapitalletter not in ["SI","NO"]:
                    print("No ingresaste las opciones especificadas. \n")
                    continue
                elif anotherdaycapitalletter == "SI":
                    while True:
                        routineday = input("Ingresa el dia que vas a agregar. Ejemplo: Lunes, Martes, Etc.. \n" \
                        "o SALIR si ya no deseas agregar DIAS: \n")
                        routinedaycl = routineday.upper()
                        if routinedaycl not in ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO", "SALIR"]:
                            print("Datos no validos.")
                            continue
                        elif routinedaycl == "SALIR":
                            break
                        else:
                            days.append(routinedaycl)
                            continue
                
                add_task(name, description, status, time, priority, days)
            except ValueError:
                print("Ingresaste valores no esperados. \n")
                continue

        elif selection == 2:
            read_task()

        elif selection == 3:
            if len(tasks) == 0:
                print("No hay tareas asignadas.")
                continue
            else:
                try:
                    number_task = int(input("Que numero de tarea quieres modificar: ")) - 1
                    #if number_task+1 < len(tasks) or number_task+1 >len(tasks): #Esta bien, pero habia
                    #un bug, si seleccionabas la tarea 1, y tenias dos tareas, entonces1-1 = 0 + 1 = 1 que era < 2  
                    if number_task < 0 or number_task >=len(tasks):
                        print(f"Numero de tarea no valido, el numero de tareas que tienes es {len(tasks)}\n")
                        continue
                    print("valores disponibles a modificar: nombre, descripcion, estado, tiempo, PRIORIDAD y DIAS. \n")
                    feature_update = input("Ingresa aqui el dato a modificar: ")
                    feature_update_cl = feature_update.upper()
                    if feature_update_cl not in ["NOMBRE","DESCRIPCION","ESTADO","TIEMPO","PRIORIDAD","DIAS"]:
                        print("Dato a modificar no valido.")
                        continue
                    elif feature_update_cl == "TIEMPO":
                        value = float(input("Ingresa el tiempo: \n"))
                        update_task(number_task, feature_update_cl, value)

                    else:
                        value = input("Ingresa la modificacion: \n")
                        update_task(number_task, feature_update_cl, value)
                except ValueError:
                    print("Ingresaste un valor incorrecto.")
                    continue
                except IndexError:
                    print("Ese numero de tarea no existe.")
                    continue

        elif selection == 4:
            if len(tasks) == 0:
                print("No hay tareas disponibles")
                continue

            print("Tareas disponibles a eliminar:")
            for indice, i in enumerate(tasks):
                print(f"Indice: {indice+1}, Nombre: {i['NOMBRE']}, Estado: {i['ESTADO']} \n")
            position = int(input("Que numero de tarea deseas eliminar: "))
            try:
                delete_task(position - 1)
            except IndexError:
                print("Ese numero de tarea no existe.")
                continue

        else:
            print("Error al elegir")
            continue

#main_app() funciona para ejecutarlo en consola, pero cuando importamos a otro codigo, necesitamos algo diferente
if __name__ == "__main__":
    main_app()

"Significa que solo se ejecute main_app() si ejecuto este archivo directamente, pero si otro archivo lo importa,"
"solo le pueda prestar sus caracteristicas o funciones y main_app() se quede callado"