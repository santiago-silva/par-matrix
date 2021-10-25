class Tweet:
    
	mensaje = ''
	user = ''
	global MAX_PALABRAS_EN_TWEET
	MAX_PALABRAS_EN_TWEET = 15

	def __init__(self, mensaje, user):
		self.mensaje = mensaje
		self.user = user

	def contienePalabra(self, palabra):
		return self.mensaje.find(palabra)

	def longitudInvalida(self):
		a = self.mensaje.split(' ')
		return len(a) > MAX_PALABRAS_EN_TWEET
	
	def	tweetDirigido(self):
		return self.mensaje.find('@') != -1

	def aQuienSeDirige(self):
		return list(filter(lambda x: x[0] in '@', self.mensaje.split(' ')))