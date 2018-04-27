from ejercicio5ClassCancion import Cancion
from ejercicio5ClassAlbum import Album
from ejercicio5ClassArtista import Artista
from ejercicio5ClassAutor import Autores
import datetime

BlackSabbath = Album()
Ozzy = Artista()
Ozzy.setnombre("Ozzy")
Ozzy.setapellido("Osbourne")
Ozzy.setFechaNac(datetime.date(1970,8,5))
Butler = Autores()
Butler.nombre = "Geezer"
Butler.apellido = "Butler"
Butler.fechaNac = datetime.date(1960,6,2)
Butler.nacionalidad = "Britanico"
Tommy = Artista()
Tommy.setnombre("Tommy")
Tommy.setapellido("Iommi")
Tommy.setFechaNac(datetime.date(1976,6,5))
Peper = Artista()
Peper.setnombre("Pepe")
Peper.setapellido("Pepeto")
Peper.fechaNac= (datetime.date(1976,6,5))
Elpepo = Cancion()
Warning = Cancion()
Elpepo.setlistaArtistas(Peper)

Warning.setlistaArtistas(Ozzy)
Warning.setlistaAutores(Butler)
Warning.setlistaArtistas(Tommy)
BlackSabbath.setListaCaciones(Warning)
BlackSabbath.setListaCaciones(Elpepo)
pepe = BlackSabbath.getListaArtista()

for i in pepe:
    print(i.nombre)




