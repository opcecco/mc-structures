#!/usr/bin/env python3

from pprint import pprint
from itertools import product

from minecraft import *


if __name__ == '__main__':

	gen = MapGenEndCity(ChunkGeneratorEnd(World(WorldInfo(-9026545427915476545))))
	coords = [(x, z) for x, z in product(range(-100, 100), range(-100, 100)) if gen.canSpawnStructureAtCoords(x, z)]
	pprint(coords)
