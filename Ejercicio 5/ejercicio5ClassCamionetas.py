from ejercicio5ClassVehiculos import Vehiculos

class Caminonetas (Vehiculos):

    def __init__(self, patente, cantidadRuedas, añoFabricacion, capacidadDeCarga):

        Vehiculos.__init__(self, patente, cantidadRuedas, añoFabricacion)

        self.capacidadDeCarga = capacidadDeCarga

    def setCapacidadDeCarga(self, capacidadDeCargaAIngresar):

        self.capacidadDeCarga = capacidadDeCargaAIngresar


