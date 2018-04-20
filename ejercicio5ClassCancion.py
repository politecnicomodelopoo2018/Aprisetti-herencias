class Cancion (object):

    nombre=None
    listaAutores = []
    listaArtistas = []

    def setnombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar

    def setlistaAutores(self, autorAIngresar):
        self.listaAutores.append(autorAIngresar)

    def setlistaArtistas(self, artistaAIngresar):
        self.listaArtistas.append(artistaAIngresar)


