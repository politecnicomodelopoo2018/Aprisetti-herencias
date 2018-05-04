from ejercicio7ClassPersona import Personas

class Profesores(Personas):

    def __init__(self, nombre, apellido, porcentajeDesc):

        Personas.__init__(self, nombre, apellido, porcentajeDesc)

        self.porcentajeDesc = porcentajeDesc

    def setPorcentajeDesc(self, porcentajeDescAIngresar):
        self.porcentajeDesc = porcentajeDescAIngresar

    def getDescuento(self):
        return self.porcentajeDesc
