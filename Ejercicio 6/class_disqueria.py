from ejercicio5ClassAlbum import Album


class Disqueria(object):
    nombre = None

    def __init__(self):
        self.lista_albums = []

    def artistaInfluyente(self):
        artistaInf = [None, 0]

        for item in self.lista_albums:
            if artistaInf[1] < item.getArtistaInfluyente[1]:
                artistaInf == item.getArtistaInfluyente

        return artistaInf[0]