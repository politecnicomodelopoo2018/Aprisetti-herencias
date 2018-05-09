from ejercicio8ClassPrograma.py import Programa
class programaMusica(Programa):

    def __init__(self, nombre, operario, categoria, musicalizador, estilo):

        Programa.__init__(self, nombre, operario, categoria, musicalizador, estilo)

        self.musicalizador = musicalizador
        self.estilo = estilo

    def setmusicalizador(self, musicalizadorAIngresar):
        self.musicalizador = musicalizadorAIngresar

    def setEstilo(self, estiloAIngresar):
        self.estilo = estiloAIngresar


