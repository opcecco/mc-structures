from math import sqrt
from javarandom import Random

from .NoiseGeneratorSimplex import NoiseGeneratorSimplex
from .NoiseGeneratorOctaves import NoiseGeneratorOctaves


class ChunkGeneratorEnd:

	def __init__(self, p1):

		self.worldObj = p1
		self.rand = Random(p1.getWorldInfo().getSeed())
		self.lperlinNoise1 = NoiseGeneratorOctaves(self.rand, 16)
		self.lperlinNoise2 = NoiseGeneratorOctaves(self.rand, 16)
		self.perlinNoise1 = NoiseGeneratorOctaves(self.rand, 8)
		self.noiseGen5 = NoiseGeneratorOctaves(self.rand, 10)
		self.noiseGen6 = NoiseGeneratorOctaves(self.rand, 16)
		self.islandNoise = NoiseGeneratorSimplex(self.rand)


	def getIslandHeightValue(self, p1, p2, p3, p4):

		f = p1 * 2 + p3
		f1 = p2 * 2 + p4
		f2 = 100 - sqrt(f * f + f1 * f1) * 8

		if f2 > 80:
			f2 = 80

		if f2 < -100:
			f2 = -100

		for i in range(-12, 13):
			for j in range(-12, 13):
				k = p1 + i
				l = p2 + j

				if k * k + l * l > 4096 and self.islandNoise.getValue(k, l) < -0.8999999761581421:
					f3 = (abs(k) * 3439 + abs(l) * 147) % 13 + 9
					f = p3 - i * 2
					f1 = p4 - j * 2
					f4 = 100 - sqrt(f * f + f1 * f1) * f3

					if f4 > 80:
						f4 = 80

					if f4 < -100:
						f4 = -100

					if f4 > f2:
						f2 = f4

		return f2


	def isIslandChunk(self, p1, p2):

		return p1 * p1 + p2 * p2 > 4096 and self.getIslandHeightValue(p1, p2, 1, 1) >= 0
