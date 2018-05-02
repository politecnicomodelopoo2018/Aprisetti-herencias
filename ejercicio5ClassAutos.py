from ejercicio5ClassVehiculos import Vehiculos

class Autos(Vehiculos):

    def __init__(self, patente, cantidadRuedas, añoFabricacion, descapotable):

        Vehiculos.__init__(self, patente, cantidadRuedas, añoFabricacion)

        self.descapotable = descapotable

    def setDescapotable(self, descapotableAIngresar):

        self.descapotable = descapotableAIngresar