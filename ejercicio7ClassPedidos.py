
class Pedidos(object):

    confirmacion = False
    listaPlatos = []

    def __init__(self, fecha, persona, hora):
        self.fecha = fecha
        self.persona = persona
        self.hora = hora


    def setfecha(self, fechaAIngresar):
        self.fecha = fechaAIngresar

    def setpersona(self, personaAIngresar):
        self.persona = personaAIngresar

    def sethora(self, horaAIngresar):
        self.hora = horaAIngresar

    def setplatos(self, platoAIngresar):
        self.listaPlatos.append(platoAIngresar)


    def
