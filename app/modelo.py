# Clase base para los objetos que se uniran a la lista de procesos 
class ALibre():
    def __init__(self, numero, localidad, tamaño, estado):
        self.numero = numero
        self.localidad = localidad
        self.tamaño = tamaño
        self.estado = estado


# Clase hija, heredamos los atributos de ALibre ya gregamos nuevos
class Particion(ALibre):
    def __init__(self, nombre, tLlegada, duracion, numero, localidad, tamaño, estado, proceso):
        super().__init__(numero, localidad, tamaño, estado)
        self.nombre = nombre
        self.tLlegada = tLlegada
        self.duracion = duracion
        self.proceso = proceso


