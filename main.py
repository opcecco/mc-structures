#!/usr/bin/env python3

from pprint import pprint
from itertools import product

from minecraft import *


if __name__ == '__main__':

	gen = MapGenEndCity(ChunkGeneratorEnd(World(WorldInfo(-9026545427915476545))))

	for x in range(-100, 100):
		for z in range(-100, 100):
			if gen.canSpawnStructureAtCoords(x, z):
				# print(f'{x}\t{z}')
				print(f'{x * 16}\t{z * 16}')
