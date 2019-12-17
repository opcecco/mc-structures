from javarandom import Random


class World:

	def __init__(self, info):

		self.worldInfo = info
		self.rand = Random()


	def setRandomSeed(self, p1, p2, p3):

		i = p1 * 341873128712 + p2 * 132897987541 + self.getWorldInfo().getSeed() + p3
		self.rand.setSeed(i)
		return self.rand


	def getWorldInfo(self):

		return self.worldInfo
