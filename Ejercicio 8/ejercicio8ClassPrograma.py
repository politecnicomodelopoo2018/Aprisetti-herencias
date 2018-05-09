
class Programa(object):

    def __init__(self, nombre, operario, categoria):

        self.nombre = nombre
        self.operario = operario
        self.categoria = categoria

        listaBloques = []
        listaConductores = []


    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setOperario(self, operarioAIngresar):
        self.operario = operarioAIngresar

    def setCategoria(self, categoriaAIngresar):
        self.categoria = categoriaAIngresar

    def addBloque(self, bloqueAIngresar):
        self.listaBloques.append(bloqueAIngresar)

    def addProductor(self, productorAIngresar):
        self.listaProductores.append(productorAIngresar)

