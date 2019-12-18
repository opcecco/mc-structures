class NoiseGeneratorImproved:

	GRAD_X = [1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0, 0, 1, 0, -1, 0]
	GRAD_Y = [1, 1, -1, -1, 0, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1]
	GRAD_Z = [0, 0, 0, 0, 1, 1, -1, -1, 1, 1, -1, -1, 0, 1, 0, -1]


	def __init__(self, p1):

		self.permutations = [0] * 512
		self.xCoord = p1.nextDouble() * 256
		self.yCoord = p1.nextDouble() * 256
		self.zCoord = p1.nextDouble() * 256

		for i in range(256):
			self.permutations[i] = i

		for l in range(256):
			j = p1.nextInt(256 - l) + l
			k = self.permutations[l]
			self.permutations[l] = self.permutations[j]
			self.permutations[j] = k
			self.permutations[l + 256] = self.permutations[l]


	def lerp(self, p1, p3, p5):

		return p3 + p1 * (p5 - p3)


	def grad(self, p1, p2, p4, p6):

		i = p1 & 15
		return self.GRAD_X[i] * p2 + self.GRAD_Y[i] * p4 + self.GRAD_Z[i] * p6


	def populateNoiseArray(self, noiseArray, xOffset, yOffset, zOffset, xSize, ySize, zSize, xScale, yScale, zScale, noiseScale):

		if ySize == 1:
			i5 = 0
			j5 = 0
			j = 0
			k5 = 0
			d14 = 0
			d15 = 0
			l5 = 0
			d16 = 1 / noiseScale

			for j2 in range(xSize):
				d17 = xOffset + j2 * xScale + self.xCoord
				i6 = int(d17)

				if d17 < i6:
					i6 -= 1

				k2 = i6 & 255
				d17 = d17 - i6
				d18 = d17 * d17 * d17 * (d17 * (d17 * 6 - 15) + 10)

				for j6 in range(zSize):
					d19 = zOffset + j6 * zScale + self.zCoord
					k6 = int(d19)

					if d19 < k6:
						k6 -= 1

					l6 = k6 & 255
					d19 = d19 - k6
					d20 = d19 * d19 * d19 * (d19 * (d19 * 6 - 15) + 10)
					i5 = self.permutations[k2] + 0
					j5 = self.permutations[i5] + l6
					j = self.permutations[k2 + 1] + 0
					k5 = self.permutations[j] + l6
					d14 = self.lerp(d18, self.grad2(self.permutations[j5], d17, d19), self.grad(self.permutations[k5], d17 - 1, 0, d19))
					d15 = self.lerp(d18, self.grad(self.permutations[j5 + 1], d17, 0, d19 - 1), self.grad(self.permutations[k5 + 1], d17 - 1, 0, d19 - 1))
					d21 = self.lerp(d20, d14, d15)
					i7 = l5
					l5 += 1
					noiseArray[i7] += d21 * d16
		else:
			i = 0
			d0 = 1 / noiseScale
			k = -1
			l = 0
			i1 = 0
			j1 = 0
			k1 = 0
			l1 = 0
			i2 = 0
			d1 = 0
			d2 = 0
			d3 = 0
			d4 = 0

			for l2 in range(xSize):
				d5 = xOffset + l2 * xScale + self.xCoord
				i3 = int(d5)

				if d5 < i3:
					i3 -= 1

				j3 = i3 & 255
				d5 = d5 - i3
				d6 = d5 * d5 * d5 * (d5 * (d5 * 6 - 15) + 10)

				for k3 in range(zSize):
					d7 = zOffset + k3 * zScale + self.zCoord
					l3 = int(d7)

					if d7 < l3:
						l3 -= 1

					i4 = l3 & 255
					d7 = d7 - l3
					d8 = d7 * d7 * d7 * (d7 * (d7 * 6 - 15) + 10)

					for j4 in range(ySize):
						d9 = yOffset + j4 * yScale + self.yCoord
						k4 = int(d9)

						if d9 < k4:
							k4 -= 1

						l4 = k4 & 255
						d9 = d9 - k4
						d10 = d9 * d9 * d9 * (d9 * (d9 * 6 - 15) + 10)

						if j4 == 0 or l4 != k:
							k = l4
							l = self.permutations[j3] + l4
							i1 = self.permutations[l] + i4
							j1 = self.permutations[l + 1] + i4
							k1 = self.permutations[j3 + 1] + l4
							l1 = self.permutations[k1] + i4
							i2 = self.permutations[k1 + 1] + i4
							d1 = self.lerp(d6, self.grad(self.permutations[i1], d5, d9, d7), self.grad(self.permutations[l1], d5 - 1, d9, d7))
							d2 = self.lerp(d6, self.grad(self.permutations[j1], d5, d9 - 1, d7), self.grad(self.permutations[i2], d5 - 1, d9 - 1, d7))
							d3 = self.lerp(d6, self.grad(self.permutations[i1 + 1], d5, d9, d7 - 1), self.grad(self.permutations[l1 + 1], d5 - 1, d9, d7 - 1))
							d4 = self.lerp(d6, self.grad(self.permutations[j1 + 1], d5, d9 - 1, d7 - 1), self.grad(self.permutations[i2 + 1], d5 - 1, d9 - 1, d7 - 1))

						d11 = self.lerp(d10, d1, d2)
						d12 = self.lerp(d10, d3, d4)
						d13 = self.lerp(d8, d11, d12)
						j7 = i
						i += 1
						noiseArray[j7] += d13 * d0
