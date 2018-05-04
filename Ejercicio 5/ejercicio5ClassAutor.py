from ejercicio5ClassPersona import Persona

class Autores(Persona):

    def __init__(self, nombre, apellido, fechaNac, nacionalidad):

        Persona.__init__((self, nombre, apellido, fechaNac))

        self.nacionalidad = nacionalidad

    def setNacionalidad(self, nacionalidad):

        self.nacionalidad = nacionalidad