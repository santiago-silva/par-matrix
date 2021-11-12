from BotPublicidad import BotPublicidad
from BotPolicia import BotPolicia

class Ronronear:
	tweets = []
	tweetsDirigidos = [] 
	tweetsNoDirigidos = []
	
	# atributos para bot policia
	listaNegra = ["bigote","enano","gordo","pelado"]
	respPolicia = "Estas violando las normas de tweets."
	
	buscarPublicidadAutos = ["auto"]
	publicidadAutos = "Los mejores autos los encontras en: www.autos.com/losMejores"

	bot = BotPolicia(listaNegra, respPolicia)
	botPubli = BotPublicidad(buscarPublicidadAutos, publicidadAutos)
	
	def recibirTweet(self, user, tweet):
		self.tweets.append(user + ": " + tweet)
		self.bot.analizarTweet(tweet, user)
		self.botPubli.buscarPalabra(tweet, user)
	
	def printTweets(self):
		if (self.tweets):
			for i in self.tweets:
				print (i)
		else:
			print ("No hay tweets")

	def auxPrintProhibido(self):
		self.bot.printTweetsProhibidos()