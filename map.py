import nbtlib
from random import*
import os,sys
import time



def load(file):
	world=nbtlib.load(f'{os.path.dirname(os.path.abspath(__file__))}//maps/{file}')
	root = world.get("ClassicWorld")
	data=bytearray(root.get("BlockArray"))

	#size
	x=root.get('X')
	y=root.get('Y')
	z=root.get('Z')

	#spawn
	spawn = root.get("Spawn")
	spawnx=spawn.get("X")
	spawny=spawn.get("Y")
	spawnz=spawn.get("Z")
	spawnh=spawn.get("H")
	spawnp=spawn.get("P")

	volume = x * y * z
	return data,x,y,z,spawnx*32,spawny*32,spawnz*32,spawnh,spawnp,volume


