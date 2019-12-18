from math import floor

from .NoiseGeneratorImproved import NoiseGeneratorImproved


class NoiseGeneratorOctaves:

	def __init__(self, seed, octavesIn):

		self.octaves = octavesIn
		self.generatorCollection = [None] * octavesIn

		for i in range(octavesIn):
			self.generatorCollection[i] = NoiseGeneratorImproved(seed)


	def generateNoiseOctaves(self, noiseArray, xOffset, yOffset, zOffset, xSize, ySize, zSize, xScale, yScale, zScale):

		if not noiseArray:
			noiseArray = [0] * (xSize * ySize * zSize)
		else:
			for i in range(len(noiseArray)):
				noiseArray[i] = 0

		d3 = 1

		for j in range(self.octaves):
			d0 = xOffset * d3 * xScale
			d1 = yOffset * d3 * yScale
			d2 = zOffset * d3 * zScale
			k = floor(d0)
			l = floor(d2)
			d0 = d0 - k
			d2 = d2 - l
			k = k % 16777216
			l = l % 16777216
			d0 = d0 + k
			d2 = d2 + l
			self.generatorCollection[j].populateNoiseArray(noiseArray, d0, d1, d2, xSize, ySize, zSize, xScale * d3, yScale * d3, zScale * d3, d3)
			d3 /= 2

		return noiseArray
