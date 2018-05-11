
from ejercicio8ClassPrograma import Programa

class programaMusica(Programa):

    def __init__(self, nombre = None, operario = None, categoria = None, musicalizador = None, estilo = None):

        Programa.__init__(self, nombre, operario, categoria)

        self.musicalizador = musicalizador
        self.estilo = estilo

    def setmusicalizador(self, musicalizadorAIngresar):
        self.musicalizador = musicalizadorAIngresar

    def setEstilo(self, estiloAIngresar):
        self.estilo = estiloAIngresar

    def codificacion(self):
        return ("%s|%s|%s|%s|%s|%s")%(self.__class__.__name__,self.nombre, self.operario.nombre, self.categoria,
                                      self.estilo, self.musicalizador.nombre)

    def decodificacion(self, datos):
        self.nombre = datos[1]
        self.operario = datos[2]
        self.categoria = datos[3]
        self.estilo = datos[4]
        self.musicalizador = datos[5]