class Pedidos(object):

    confirmacion = False

    def __init__(self, fecha, persona, hora):
        self.fecha = fecha
        self.persona = persona
        self.hora = hora
        self.listaPlatosEnPedido = []

    def setFecha(self, fechaAIngresar):
        self.fecha = fechaAIngresar

    def setPersona(self, personaAIngresar):
        self.persona = personaAIngresar

    def setHora(self, horaAIngresar):
        self.hora = horaAIngresar

    def addPlatos(self, platoAIngresar):
        self.listaPlatos.append(platoAIngresar)

    def setPlatos(self, listaPlatosAIngresar):
        self.listaPlatos = listaPlatosAIngresar

    def getprecioPlatos(self):
        for precioTotal in self.listaPlatosEnPedido:
            precioTotal += precioTotal.precio

    def getPrecio(self):
        return self.persona.getDescuento * self.getprecioPlatos()


