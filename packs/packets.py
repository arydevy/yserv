from packs.settings import *
import hashlib
import gzip
import struct
from packs.packfun import*
from packs.wr import*



#================Pack class start ==================#

def client_server(client):
	id=read_byte(client)
	print(id)
	#player identification
	if id == '0x00' or '\x00':player_join(client)
	#set block
	if id == '0x05':set_block(p)
	#player orentation and position
	if id == '0x08':pass
	if id == '0x0d':pass

def server_client(client):
	pass
#================Pack class end======================#
