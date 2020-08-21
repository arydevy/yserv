#================read write functions start=========#
def read_byte(client):
	return client.recv(1)

def read_string(client):
	return str(client.recv(64),'utf-8')

def write_byte(client,data):
	client.send(struct.pack('>B', data))

def write_string(client,data):
	data = bytes(data, 'utf-8')
	client.send(struct.pack('64s', data))
	
def write_short(client,data):
	client.send(struct.pack('>H', data))


#================read write functions end===========#