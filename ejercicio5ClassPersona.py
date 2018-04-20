class Persona(object):

    nombre = None
    apellido = None
    fechaNac = None

    def setnombre(self , nombrePersonaAIngresar):
        self.nombre= nombrePersonaAIngresar

    def setapellido(self, apellidoPersonaAIngresar):
        self.apellido = apellidoPersonaAIngresar

    def setFechaNac(self, fechaNacAIngresar):
        self.fechaNac = fechaNacAIngresar


class Autores(Persona):
    nacionalidad = None

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad



class Artista(Persona):
    pass


