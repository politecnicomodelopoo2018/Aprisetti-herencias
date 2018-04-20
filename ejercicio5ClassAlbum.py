class Album (object):

    nombre= None

    def __init__(self):
        self.listaCanciones = []


    def setnombre (self, nombreAIngresar):
        self.nombre= nombreAIngresar

    def setListaCaciones(self, cancionAIngresar):
        self.listaCanciones.append(cancionAIngresar)


    def getListaArtista(self, albumAIngresar):
        listaArtistasAlbum = []

        for cancion in albumAIngresar.listaCanciones:
            for artista in cancion.listaArtistas:
                if not artista in listaArtistasAlbum:
                    listaArtistasAlbum.append(artista)


        return listaArtistasAlbum

    def getArtistaInfluyente(self, albumAIngresar1):
        Max = 0
        Try = 0

        for cancion in albumAIngresar1.listaCanciones:
            for artista in cancion.listaArtistas