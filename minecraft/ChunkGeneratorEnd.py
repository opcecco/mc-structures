from math import sqrt
from javarandom import Random

from .NoiseGeneratorSimplex import NoiseGeneratorSimplex
from .NoiseGeneratorOctaves import NoiseGeneratorOctaves


class ChunkGeneratorEnd:

	AIR = 0
	END_STONE = 1


	def __init__(self, p1):

		self.worldObj = p1
		self.rand = Random(p1.getWorldInfo().getSeed())
		self.lperlinNoise1 = NoiseGeneratorOctaves(self.rand, 16)
		self.lperlinNoise2 = NoiseGeneratorOctaves(self.rand, 16)
		self.perlinNoise1 = NoiseGeneratorOctaves(self.rand, 8)
		self.noiseGen5 = NoiseGeneratorOctaves(self.rand, 10)
		self.noiseGen6 = NoiseGeneratorOctaves(self.rand, 16)
		self.islandNoise = NoiseGeneratorSimplex(self.rand)
		self.buffer = None
		self.pnr = None
		self.ar = None
		self.br = None


	def setBlocksInChunk(self, x, z, primer):

		i = 2
		j = 3
		k = 33
		l = 3
		self.buffer = self.getHeights(self.buffer, x * 2, 0, z * 2, 3, 33, 3)

		for i1 in range(2):
			for j1 in range(2):
				for k1 in range(32):
					d0 = 0.25
					d1 = self.buffer[((i1 + 0) * 3 + j1 + 0) * 33 + k1 + 0]
					d2 = self.buffer[((i1 + 0) * 3 + j1 + 1) * 33 + k1 + 0]
					d3 = self.buffer[((i1 + 1) * 3 + j1 + 0) * 33 + k1 + 0]
					d4 = self.buffer[((i1 + 1) * 3 + j1 + 1) * 33 + k1 + 0]
					d5 = (self.buffer[((i1 + 0) * 3 + j1 + 0) * 33 + k1 + 1] - d1) * 0.25
					d6 = (self.buffer[((i1 + 0) * 3 + j1 + 1) * 33 + k1 + 1] - d2) * 0.25
					d7 = (self.buffer[((i1 + 1) * 3 + j1 + 0) * 33 + k1 + 1] - d3) * 0.25
					d8 = (self.buffer[((i1 + 1) * 3 + j1 + 1) * 33 + k1 + 1] - d4) * 0.25

					for l1 in range(4):
						d9 = 0.125
						d10 = d1
						d11 = d2
						d12 = (d3 - d1) * 0.125
						d13 = (d4 - d2) * 0.125

						for i2 in range(8):
							d14 = 0.125
							d15 = d10
							d16 = (d11 - d10) * 0.125

							for j2 in range(8):
								iblockstate = self.AIR

								if d15 > 0:
									iblockstate = self.END_STONE

								k2 = i2 + i1 * 8
								l2 = l1 + k1 * 4
								i3 = j2 + j1 * 8
								primer.setBlockState(k2, l2, i3, iblockstate)
								d15 += d16

							d10 += d12
							d11 += d13

						d1 += d5
						d2 += d6
						d3 += d7
						d4 += d8


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


	def getHeights(self, p1, p2, p3, p4, p5, p6, p7):

		if not p1:
			p1 = [0] * (p5 * p6 * p7)

		d0 = 684.412
		d1 = 684.412
		d0 = d0 * 2
		self.pnr = self.perlinNoise1.generateNoiseOctaves(self.pnr, p2, p3, p4, p5, p6, p7, d0 / 80, 4.277575000000001, d0 / 80)
		self.ar = self.lperlinNoise1.generateNoiseOctaves(self.ar, p2, p3, p4, p5, p6, p7, d0, 684.412, d0)
		self.br = self.lperlinNoise2.generateNoiseOctaves(self.br, p2, p3, p4, p5, p6, p7, d0, 684.412, d0)
		i = int(p2 / 2)
		j = int(p4 / 2)
		k = 0

		for l in range(p5):
			for i1 in range(p7):
				f = self.getIslandHeightValue(i, j, l, i1)

				for j1 in range(p6):
					d2 = self.ar[k] / 512
					d3 = self.br[k] / 512
					d5 = (self.pnr[k] / 10 + 1) / 2

					if d5 < 0:
						d4 = d2
					elif d5 > 1:
						d4 = d3
					else:
						d4 = d2 + (d3 - d2) * d5

					d4 = d4 - 8
					d4 = d4 + f
					k1 = 2

					if j1 > p6 / 2 - k1:
						d6 = (j1 - (p6 / 2 - k1)) / 64
						d6 = min(max(d6, 0), 1)
						d4 = d4 * (1 - d6) + -3000 * d6

					k1 = 8

					if j1 < k1:
						d7 = (k1 - j1) / (k1 - 1)
						d4 = d4 * (1 - d7) + -30 * d7

					p1[k] = d4
					k += 1

		return p1
