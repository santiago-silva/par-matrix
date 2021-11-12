from Ronronear import *

class Main():
	ronronear = Ronronear()

	usuario = "@"+input("Ingrese su usuario: ")
	print("     ########################################\n")
	print("     Hola!! Bienvenido/a "+usuario+ " a Ronronear!!\n")
	print("     ########################################\n")
	while (True):
		try:
			op = int(input("1. Add tweet\n2. Cambiar de usuario\n3. Ver usuarios - tweets\n4. Ver comentarios prohibidos\n5. Salir\n"))
		
			if(op==5): 
				break
			else:
				if (op==2):
					usuario = "@"+input("Ingrese su usuario: ")
					print("     ########################################\n")
					print("     Hola!! Bienvenido/a "+usuario+ " a Ronronear!!\n")
					print("     ########################################")
				elif (op==1):
					myTweet = input("Add tweet: ")
					if (len(myTweet.split(' '))>15):
						print ("Por favor, el tweet debe tener solo 15 palabras")
					else:
						ronronear.recibirTweet(usuario,myTweet)
				elif (op==3):
					ronronear.printTweets()
				elif (op==4):
					ronronear.auxPrintProhibido()

		except ValueError:
			print ("Por favor, ingrese una opcion correcta")

	print ("Hasta la proxima")