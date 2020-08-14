from settings import *
import socket

USERS=0



#server thinghs
#s is server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect 
s.connect(("classicube.net",80))

#send the hertbeast
s.sendall(b"GET /heartbeat.jsp?port=25565&max=20&name=Test&public=True&version=7&salt=5555 HTTP/1.1\r\nHost:www.classicube.net\r\n\r\n")

while True:
	print(str(s.recv(3000), 'utf-8'))
