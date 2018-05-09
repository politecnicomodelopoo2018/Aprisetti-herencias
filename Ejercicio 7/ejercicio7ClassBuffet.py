class Buffet (object):

    def __init__(self):

        self.listaPedidos = []
        self.listaPlatosEnBuffet = []
        self.listaPersonas = []


    def addlistaPedidos(self , pedidoAIngresar):
        self.listaPedidos.append(pedidoAIngresar)

    def addlistaPlatos(self, platoAIngresar):
        self.listaPlatos.append(platoAIngresar)

    def addlistaPersonas(self, personaAIngresar):
        self.listaPersonas.append(personaAIngresar)

    def erasePedido(self, pedidoABorrar):

         self.listaPedidos.remove(pedidoABorrar)

    def erasePersona(self, personaABorrar):

        for item in self.listaPedidos:
            if item.persona == personaABorrar:
                self.listaPedidos.remove(item)
        self.listaPersonas.remove(personaABorrar)

    def erasePlatoDePedido(self, platoABorrar):

        for item in self.listaPedidos:
            if platoABorrar in item.l   istaPlatosEnPedido:
                self.listaPedidos.remove(item)
        self.listaPlatosEnBuffet.remove(platoABorrar)

    



