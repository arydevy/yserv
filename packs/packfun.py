from packs.wr import*
from packs.settings import *
import hashlib
WIDTH=128
HEIGHT=32
LENGTH=128
from packs.settings import *
from DB import *
import hashlib
from map import Map
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
	mapsend(client)
	spownPlayer(client,username,100,1000,100,0,0)

def mapsend(client):
	#init 
	write_byte(client,0x02)
	#send level
	#main=Map(10, 10, 10, 'main')
	#main.load('main.cw')
	
	map = bytearray(WIDTH * HEIGHT * LENGTH)

	input = struct.pack('>I', len(map)) + map
	output = gzip.compress(input)

	for i in range(0, len(output), 1024):
		chunk = output[i: i + 1024]
		client.send(struct.pack('>BH1024sB', 0x03, len(chunk), chunk, 0x00))
		print('sending')
	#map end
	write_byte(client,0x04)
	write_short(client,WIDTH)
	write_short(client,HEIGHT)
	write_short(client,LENGTH)
	print('map send')

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
#===============PACK functions end===================#