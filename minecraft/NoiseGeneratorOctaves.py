from .NoiseGeneratorImproved import NoiseGeneratorImproved


class NoiseGeneratorOctaves:

	def __init__(self, seed, octavesIn):

		self.octaves = octavesIn
		self.generatorCollection = [None] * octavesIn

		for i in range(octavesIn):
			self.generatorCollection[i] = NoiseGeneratorImproved(seed)
