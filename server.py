from packs.settings import *
import socket
from packs import *
from packs.packets import*
from os import system
#import term

USERS=0

heart=bytes(f"GET /heartbeat.jsp?port={PORT}&max={MAX}&name={NAME}&public={PUBLIC}&version=7&salt={SALT} HTTP/1.1\r\nHost:www.classicube.net\r\n\r\n",encoding="utf-8")

#server thinghs
#s is server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect 
s.connect(("classicube.net",80))

#send the hertbeat
s.sendall(heart)


# get the responce
print(str(s.recv(3000), 'utf-8'))


#####SERVER#####

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('',PORT))
server.listen(5)
on=True
##server main loop 
while on:
	#accept connections 
	(client, addr) = server.accept()
	print(client)
	#print(str(client.recv(10), 'utf-8'))

	client_server(client)
	


#####CLOSE THE SERVERS###
server.close()
s.close()

system('clear')