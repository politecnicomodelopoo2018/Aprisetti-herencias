class Personas(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido

    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setApellido(self, apellidoAIngresar):
        self.apellido = apellidoAIngresar

    def getDescuento(self):
        return 1