from Tweet import *

class pdpwitter:
	tweets = []
	tweetsDirigidos = []
	tweetsNoDirigidos = []
	bots = []

	def recibirTweet(self, tweet):
    
		if tweet.longitudInvalida():
    			print("Tweet invalido: Longitud de palabras excede el maximo permitido")
    			return "a"
		else:
			self.tweets.append(tweet)
			
			if tweet.tweetDirigido():
				self.tweetsDirigidos.append(tweet)
			else:
				self.tweetsNoDirigidos.append(tweet)

	def addBot(self, bot):
		self.bots.append(bot)



tweet = Tweet('tweet con tag @sspalisa', 'sspalisa')

print(tweet.mensaje)
print(tweet.user)
print(tweet.longitudInvalida())
print(tweet.tweetDirigido())
print(tweet.aQuienSeDirige())