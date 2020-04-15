from app import app
from app.modelo import ALibre, Particion
from flask import render_template, request, redirect

listaProcesos = [
    ["A", 8, 1, 7],
    ["B", 14, 2, 7],
    ["C", 18, 3, 4],
    ["D", 6, 4, 6],
    ["E", 14, 5, 5]
]

listaAL = []
listaAL.append(ALibre(1, 10, 54, "D"))

listaPart = []


# Utilizamos una lista para manejar el contador del tiempo, agregando elementos por cada unidad del tiempo
listaTiempo = []

def concatenacionAL():
    for proceso in listaAL:
        
        # Seccion de la memoria que verificamos si se puede concatenar
        AL = proceso.localidad + proceso.tamaño

        cont = 0 # Contador para el for

        for proceso2 in listaAL:
            # Verificacion si existe un area libre despues de otra
            if proceso2.localidad == AL:
                # Concatenamos los espacios
                proceso.tamaño += proceso2.tamaño
                
                # Por ultimo eliminamos el espacio al haberlo ya concatenado
                listaAL.pop(cont)
            
            # En caso de no cumplir con la condicion elevamos el contador
            cont +=1
                

def creacionParticion(proceso, cont):
    for aLibre in listaAL:
        # Verificacion si existe un especio libre para el proceso
        if proceso[1] <= aLibre.tamaño:
            NP = len(listaPart) + 1

            # Creamos creamos y agregamos un nuevo proceso a lista de particiones
            listaPart.append(Particion(
                proceso[0], proceso[2], proceso[3], NP, aLibre.localidad, proceso[1], "U", "P"+str(NP)))

            # Hacemos las modificaciones a el espacio libre que utilizamos
            aLibre.localidad += proceso[1]
            aLibre.tamaño -= proceso[1]

            # Eliminamos el proceso utilizado
            listaProcesos.pop(cont)
    


@app.route("/mvt", methods=["GET", "POST"])
def mvt():
    
    # Verificacion de un nuevo POST en la aplicacion
    if request.method == "POST":
        listaTiempo.append(0)

        # Verificacion si existen elementos en la lista de particiones
        if len(listaPart) != 0:
            cont = 0  # Contador para el for
            elemElim = -1
            for proceso in listaPart:
                proceso.duracion -= 1  # Restamos un tiempo a la duracion del proceso

                # Verificacion si el proceso termino
                if proceso.duracion == 0:
                    
                    # Creamos una nueva area libre y la agregamos a la lista
                    listaAL.append(
                        ALibre(len(listaAL)+1, proceso.localidad, proceso.tamaño, "D"))

                    # Lamamos a la funcion para concatenar las posibles areas libres que se puedan
                    concatenacionAL()

                    # Guardamos el numero del elemento que se modifico
                    elemElim = cont
                    

                cont += 1
            
            # Verificacion si existe un elemento a eliminar
            if elemElim != -1: 
                listaPart.pop(elemElim)


        cont = 0  # Contador para el for
        for proceso in listaProcesos:
            # Verificacion si algun proceso llega al momento del tiempo
            if proceso[2] == len(listaTiempo):
                # Llamado a la funcion para la creacion de una particion de ser posible
                creacionParticion(proceso, cont)

                # Enviamos los datos
                return render_template("mvt.html", listaP=listaProcesos, listaALibres=listaAL, listaPart=listaPart, contador = len(listaTiempo))

            if proceso[2] <= len(listaTiempo):
                # Llamado a la funcion para la creacion de una particion de ser posible
                creacionParticion(proceso, cont)

                # Enviamos los datos
                return render_template("mvt.html", listaP=listaProcesos, listaALibres=listaAL, listaPart=listaPart, contador = len(listaTiempo))

        concatenacionAL()
        
    
    return render_template("mvt.html", listaP=listaProcesos, listaALibres=listaAL, listaPart=listaPart, contador = len(listaTiempo))
