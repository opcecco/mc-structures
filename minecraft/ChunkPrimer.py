class ChunkPrimer:

	DEFAULT_STATE = 0


	def __init__(self):

		self.data = [0] * 65536


	def getBlockState(self, x, y, z):

		iblockstate = self.data[self.getBlockIndex(x, y, z)]
		return self.DEFAULT_STATE if not iblockstate else iblockstate


	def setBlockState(self, x, y, z, state):

		self.data[self.getBlockIndex(x, y, z)] = state


	@staticmethod
	def getBlockIndex(x, y, z):

		return x << 12 | z << 8 | y


	def findGroundBlockIdx(self, x, z):

		i = (x << 12 | z << 8) + 256 - 1

		for j in range(255, -1, -1):
			iblockstate = self.data[i + j]

			if iblockstate and iblockstate != self.DEFAULT_STATE:
				return j

		return 0
