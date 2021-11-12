from BotBusqueda import BotBusqueda

class BotPolicia(BotBusqueda):
    
    tweetsAnalizados = []

    def analizarTweet(self, palabra, user):
        if self.buscarPalabra(palabra, user):
            self.tweetsAnalizados.append(user + ": " + palabra)
    
    def printTweetsProhibidos(self):
        if (self.tweetsAnalizados):
            for i in self.tweetsAnalizados:
                print (i)
        else:
            print ("No hay tweets")