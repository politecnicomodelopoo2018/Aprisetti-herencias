class Vehiculos(object):

    def __init__(self, patente, cantidadRuedas, añoFabricacion):

            self.patente = patente
            self.cantidadRuedas = cantidadRuedas
            self.añoFabricacion = añoFabricacion

    def setPatente(self, patenteAIngresar):
        self.patente = patenteAIngresar

    def setCantidadRuedas(self, cantidadRuedasAIngresar):
        self.cantidadRuedas = cantidadRuedasAIngresar

    def setAñoFabricacion(self, añoFabricacionAIngresar):
        self.añoFabricacion = añoFabricacionAIngresar
