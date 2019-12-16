#!/usr/bin/env python3

from mapgenstructure import *


class MapGenEndCity:

	def __init__(self):

		pass


	def canSpawnStructureAtCoords(self, chunkX, chunkZ):

		i = chunkX
		j = chunkZ

		if chunkX < 0:
			chunkX -= 19

		if chunkZ < 0:
			chunkZ -= 19

		k = int(chunkX / 20)
		l = int(chunkZ / 20)
		random = self.worldObj.setRandomSeed(k, l, 10387313)
		k = k * 20
		l = l * 20
		k = k + int((random.nextInt(9) + random.nextInt(9)) / 2)
		l = l + int((random.nextInt(9) + random.nextInt(9)) / 2)

		if i == k and j == l and self.endProvider.isIslandChunk(i, j):
			# int i1 = func_191070_b(i, j, this.endProvider);
			# return i1 >= 60;
			return True
		else:
			return False
