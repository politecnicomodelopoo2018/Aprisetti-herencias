
class Persona (object):

    def __init__(self, nombre, apellido, fechaNac):

        self.nombre = nombre
        self.apellido=apellido
        self.fechaNac=fechaNac



class Autores (Persona):

    def __init__(self , nombre , apellido , fechaNac , nacionalidad):

        Persona.__init__ ( self, nombre, apellido, fechaNac)
        self.nacionalidad= nacionalidad



class Artista (Persona):
    pass