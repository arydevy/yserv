import nbtlib
from random import*
import os,sys
import time

class Map():
	def __init__(self,width,hight,lenght,name):
		self.x=width
		self.y=hight
		self.z=lenght
		self.name=name
		self.data

		#spown
		self.spownx
		self.spowny
		self.spownz
		self.spownh
		self.spownp

		#volume
		self.volume

	def load(self,file):
		world=nbtlib.load(f'map/{file}')
		root = level.get("ClassicWorld")
		self.data=bytearray(root.get("BlockArray"))

		#size
		self.x=root.get('X')
		self.x=root.get('Y')
		self.x=root.get('Z')

		#spawn
		spawn = root.get("Spawn")
		self.spownx=spawn.get("X")
		self.spowny=spawn.get("Y")
		self.spownz=spawn.get("Z")
		self.spownh=spawn.get("H")
		self.spownp=spawn.get("P")

		self.volume = self.x * self.y * self.z

	def set_block(self,Position,block_id):
		index = position.x + (position.z * self.size.x) + ((self.size.x * self.size.z) * position.y)
		if index < len(self.data):
			self.data[index] = block_id
