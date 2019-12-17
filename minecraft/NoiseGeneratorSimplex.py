from math import sqrt, floor


class NoiseGeneratorSimplex:

	grad3 = [[1, 1, 0], [-1, 1, 0], [1, -1, 0], [-1, -1, 0], [1, 0, 1], [-1, 0, 1], [1, 0, -1], [-1, 0, -1], [0, 1, 1], [0, -1, 1], [0, 1, -1], [0, -1, -1]]
	SQRT_3 = sqrt(3)


	def __init__(self, p1):

		self.p = [0] * 512
		self.xo = p1.nextDouble() * 256
		self.yo = p1.nextDouble() * 256
		self.zo = p1.nextDouble() * 256

		for i in range(256):
			self.p[i] = i

		for l in range(256):
			j = p1.nextInt(256 - l) + l
			k = self.p[l]
			self.p[l] = self.p[j]
			self.p[j] = k
			self.p[l + 256] = self.p[l]


	def dot(p0, p1, p3):

		return p0[0] * p1 + p0[1] * p3


	def getValue(self, p1, p3):

		d3 = 0.5 * (NoiseGeneratorSimplex.SQRT_3 - 1)
		d4 = (p1 + p3) * d3
		i = floor(p1 + d4)
		j = floor(p3 + d4)
		d5 = (3 - NoiseGeneratorSimplex.SQRT_3) / 6
		d6 = (i + j) * d5
		d7 = i - d6
		d8 = j - d6
		d9 = p1 - d7
		d10 = p3 - d8

		if d9 > d10:
			k = 1
			l = 0
		else:
			k = 0
			l = 1

		d11 = d9 - k + d5
		d12 = d10 - l + d5
		d13 = d9 - 1 + 2 * d5
		d14 = d10 - 1 + 2 * d5
		i1 = i & 255
		j1 = j & 255
		k1 = self.p[i1 + self.p[j1]] % 12
		l1 = self.p[i1 + k + self.p[j1 + l]] % 12
		i2 = self.p[i1 + 1 + self.p[j1 + 1]] % 12
		d15 = 0.5 - d9 * d9 - d10 * d10

		if d15 < 0:
			d0 = 0
		else:
			d15 = d15 * d15
			d0 = d15 * d15 * NoiseGeneratorSimplex.dot(NoiseGeneratorSimplex.grad3[k1], d9, d10)

		d16 = 0.5 - d11 * d11 - d12 * d12

		if d16 < 0:
			d1 = 0
		else:
			d16 = d16 * d16
			d1 = d16 * d16 * NoiseGeneratorSimplex.dot(NoiseGeneratorSimplex.grad3[l1], d11, d12)

		d17 = 0.5 - d13 * d13 - d14 * d14

		if d17 < 0:
			d2 = 0
		else:
			d17 = d17 * d17
			d2 = d17 * d17 * NoiseGeneratorSimplex.dot(NoiseGeneratorSimplex.grad3[i2], d13, d14)

		return 70 * (d0 + d1 + d2)
