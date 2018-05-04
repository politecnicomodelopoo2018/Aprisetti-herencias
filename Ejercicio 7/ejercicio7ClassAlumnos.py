from ejercicio7ClassPersonas import Personas

class Alumnos(Personas):

    def __init__(self, nombre, apellido, division):

        Personas.__init__(self, nombre, apellido)

        self.division = division

    def setDivision(self, divisionAIngresar):
        self.division = divisionAIngresar