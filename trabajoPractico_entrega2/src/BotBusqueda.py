
class BotBusqueda():
    
    palabraBuscada = []
    respuesta = ""
    tweetsAInvestigar = []


    def __init__(self, buscar, respuesta):
        self.palabraBuscada = buscar
        self.respuesta = respuesta
    
    def buscarPalabra(self, palabra, user):
        
        for palabraABuscar in self.palabraBuscada:
            if palabraABuscar in palabra:
                print("\n" + self.respuesta + " " + user + "\n")
                return True