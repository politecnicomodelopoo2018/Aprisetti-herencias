import datetime
class Persona(object):

    def __init__(self, nombre, apellido, dni, fechaNac, rol):

        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fechaNac = fechaNac
        self.rol = rol

    def setnombre(self , nombrePersonaAIngresar):
        self.nombre = nombrePersonaAIngresar

    def setapellido(self, apellidoPersonaAIngresar):
        self.apellido = apellidoPersonaAIngresar

    def setFechaNac(self, fechaNacAIngresar):
        self.fechaNac = fechaNacAIngresar

    def setDni(self, dniAIngresar):
        self.dni = dniAIngresar

    def setRol(self, rolAIngresar):
        self.rol = rolAIngresar

    def codificacion(self):
        return ("%s|%s|%s|%s|%s")%(self.nombre, self.apellido, self.dni, self.fechaNac.strftime("%Y/%m/%d"), self.rol)
