
class Programa(object):

    def __init__(self, nombre = None, operario = None, categoria = None):

        self.nombre = nombre
        self.operario = operario
        self.categoria = categoria

        self.listaBloques = []
        self.listaConductores = []


    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setOperario(self, operarioAIngresar):
        self.operario = operarioAIngresar

    def setCategoria(self, categoriaAIngresar):
        self.categoria = categoriaAIngresar

    def addBloque(self, bloqueAIngresar):
        self.listaBloques.append(bloqueAIngresar)

    def addConductor(self, conductorAIngresar):
        self.listaConductores.append(conductorAIngresar)

    def checkHorario(self, bloque):
        for item in self.listaBloques:
            for check in bloque:
                if check.dia == item.dia and check.horario == item.horario:
                    return True
        return False

    def codificacion(self):
        return ("%s|%s|%s|%s")%(self.__class__.__name__,self.nombre, self.operario.nombre, self.categoria)

    def decodificacion(self, datos):
        self.nombre = datos[1]
        self.operario = datos[2]
        self.categoria = datos[3]