class NoiseGeneratorImproved:

	def __init__(self, p1):

		self.permutations = [0] * 512
		self.xCoord = p1.nextDouble() * 256
		self.yCoord = p1.nextDouble() * 256
		self.zCoord = p1.nextDouble() * 256

		for i in range(256):
			self.permutations[i] = [i]

		for l in range(256):
			j = p1.nextInt(256 - l) + l
			k = self.permutations[l]
			self.permutations[l] = self.permutations[j]
			self.permutations[j] = k
			self.permutations[l + 256] = self.permutations[l]
