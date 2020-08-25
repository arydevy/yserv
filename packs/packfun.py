from packs.wr import*
from packs.settings import *
import hashlib
from packs.settings import *
from packs.online import users
import hashlib
from map import *
import gzip
import struct



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
		join(client,username)
	else:
		print(f'{username} tryed to join the server!')
		print('or joined via directconnect!!!')
		join(client,username)


def join(client,username):
	users.append(client)
	#pack id
	write_byte(client,0x00)
	#protocol version
	write_byte(client,0x07)
	#name and Motd 
	write_string(client,NAME)
	write_string(client,MOTD)
	#usertype
	write_byte(client,0x00)
	#send the map and spown the player
	for i in users:
		cl=users[i]
	data,spawnx,spawny,spawnz,spawnh,spawnp=mapsend(cl)
	spownPlayer(cl,username,spawnx,spawny,spawnz,spawnh,spawnp)

def mapsend(client):
	#init 
	write_byte(client,0x02)
	#send level
	data,x,y,z,spawnx,spawny,spawnz,spawnh,spawnp,volume=load('main.cw')
	
	#map = bytearray(x* y * z)

	input = struct.pack('>I', len(data)) + data
	output = gzip.compress(input)

	for i in range(0, len(output), 1024):
		chunk = output[i: i + 1024]
		client.send(struct.pack('>BH1024sB', 0x03, len(chunk), chunk, 0x00))
	#map end
	write_byte(client,0x04)
	write_short(client,x)
	write_short(client,y)
	write_short(client,z)
	print('map send')
	return data,spawnx,spawny,spawnz,spawnh,spawnp

def spownPlayer(client,user,x,y,z,i,h):
	#send pkid
	write_byte(client,0x07)
	write_byte(client,255)
	write_string(client,user)
	write_short(client,x)#x
	write_short(client,y)#y
	write_short(client,z)#z
	#y h
	write_byte(client,i)
	write_byte(client,h)

#set_block
def set_block(data,Position,block_id,x,y,z):
		index = position.x + (position.z * x) + ((x * z) * position.y)
		if index < len(data):
			data[index] = block_id
#===============PACK functions end===================#