from settings import *
from DB import *
import hashlib
from map import Map
import gzip
import struct
WIDTH=128
HEIGHT=32
LENGTH=128

#================read write functions start=========#
def read_byte(client):
	return client.recv(1)

def read_string(client):
	return str(client.recv(64),'utf-8')

def write_byte(client,data):
	client.send(bytes(data))

def write_string(client,data):
	client.send(bytes(data,'utf-8'))
def write_num(client,input):
	client.send(bytes(input))


#================read write functions end===========#

#================Pack class start ==================#

def client_server(client):
	id=read_byte(client)
	print(id)
	#player identification
	if id == '0x00' or '\x00':player_join(client)
	#set block
	if id == '0x05':pass
	#player orentation and position
	if id == '0x08':pass
	if id == '0x0d':pass

def server_client(client):
	pass
#================Pack class end======================#
#===============PACK functions start=================#

def player_join(client):
	#get player info
	protocol_version=read_byte(client)
	username=read_string(client)
	ver_key=read_string(client)
	unused=read_byte(client)

	#autetyficate the player
	data = (SALT+username).encode('utf-8')
	if ver_key == hashlib.md5(data).hexdigest():
		print(f'{username} joined!')
		join(client)
	else:
		print(f'{username} tryed to join the server!')
		print('or joined via directconnect!!!')
		join(client)


def join(client):
	#pack id
	write_byte(client,bytes(0x00))
	#protocol version
	write_byte(client, bytes(0x07))
	#name and Motd 
	write_string(client,NAME)
	write_string(client,MOTD)
	#usertype
	write_byte(client,bytes(0x00))
	mapsend(client)
	spownPlayer(client)

def mapsend(client):
	#init 
	write_byte(client,0x02)
	#send level
	#main=Map(10, 10, 10, 'main')
	#main.load('main.cw')
	
	map = bytearray(WIDTH * HEIGHT * LENGTH)

	def send(data):
		write_byte(client, data)

	def send_():
		input = struct.pack('>I', len(map)) + map
		output = gzip.compress(input)

		send(struct.pack('<B', 0x02))
		for i in range(0, len(output), 1024):
			chunk = output[i: i + 1024]
			send(struct.pack('<BH1024sB', 0x03, len(chunk), chunk, 0x00))
			send(struct.pack('<BHHH', 0x04, WIDTH, HEIGHT, LENGTH))
			print('sending')
	send_()
	#map sendet
	write_byte(client,0x04)
	print('map send')

def spownPlayer(client):
	#send pkid
	write_byte(client,0x07)
	write_byte(client, 255)
	write_string(client,'arydev')
	write_num(client,0)#x
	write_num(client,100)#y
	write_num(client,0)#z
	#y h
	write_byte(client,0)
	write_byte(client,0)
#===============PACK functions end===================#