from ejercicio5ClassArtista import Artista

class Album (object):

    nombre= None

    def __init__(self):
        self.listaCanciones = []

    def setnombre (self, nombreAIngresar):
        self.nombre= nombreAIngresar

    def setListaCaciones(self, cancionAIngresar):
        self.listaCanciones.append(cancionAIngresar)


    def getListaArtista(self):
        listaArtistasAlbum = []

        for cancion in self.listaCanciones:
            for artista in cancion.listaArtistas:
                if not artista in listaArtistasAlbum:
                    listaArtistasAlbum.append(artista)
        return listaArtistasAlbum

    def getArtistaInfluyente(self):
        artistaMayor = Artista()
        count = 0
        count2 = 0

        listaArtista = self.getListaArtista()

        for cancion in self.listaCanciones:
            for artistaUno in cancion.listaArtistas:
                if(count2 < count):
                    count2 == count
                count = 0
                for artistaDos in listaArtista:
                    if(artistaUno == artistaDos):
                        count += 1
                    if(count > count2):
                        artistaMayor = artistaUno
        return artistaMayor, count


    def getCancionesPorNacionalidad(self, nacionalidadAIngresar):

        listaCanciones = []

        for item in self.listaCanciones:
           for autor in item.listaAutores:
               if autor.nacionalidad == nacionalidadAIngresar:
                   listaCanciones.append(item)

        return listaCanciones



