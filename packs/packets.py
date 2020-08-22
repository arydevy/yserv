from packs.settings import *
from DB import *
import hashlib
from map import Map
import gzip
import struct
from packs.packfun import*
from packs.wr import*


WIDTH=128
HEIGHT=32
LENGTH=128



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
