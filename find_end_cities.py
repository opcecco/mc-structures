#!/usr/bin/env python3

import sys
import json
from math import sqrt, floor
from pprint import pprint
from itertools import product
from javarandom import Random


SQRT_3 = sqrt(3)
grad3 = [[1, 1, 0], [ -1, 1, 0], [1, -1, 0], [ -1, -1, 0], [1, 0, 1], [ -1, 0, 1], [1, 0, -1], [ -1, 0, -1], [0, 1, 1], [0, -1, 1], [0, 1, -1], [0, -1, -1]]

noise_p = [0] * 512

world_seed = -9026545427915476545
rand = Random(world_seed)


for i in range(66):
	garbage = rand.nextDouble()
	garbage = rand.nextDouble()
	garbage = rand.nextDouble()

	for l in range(256):
		garbage = rand.nextInt(256 - l) + l

garbage = rand.nextDouble()
garbage = rand.nextDouble()
garbage = rand.nextDouble()

for i in range(256):
	noise_p[i] = i

for l in range(256):
	j = rand.nextInt(256 - l) + l
	k = noise_p[l]
	noise_p[l] = noise_p[j]
	noise_p[j] = k
	noise_p[l + 256] = noise_p[l]


def dot(p0, p1, p3):

	return p0[0] * p1 + p0[1] * p3


def noise_get_value(p1, p3):

	d3 = 0.5 * (SQRT_3 - 1)
	d4 = (p1 + p3) * d3
	i = floor(p1 + d4)
	j = floor(p3 + d4)
	d5 = (3 - SQRT_3) / 6
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
	k1 = noise_p[i1 + noise_p[j1]] % 12
	l1 = noise_p[i1 + k + noise_p[j1 + l]] % 12
	i2 = noise_p[i1 + 1 + noise_p[j1 + 1]] % 12
	d15 = 0.5 - d9 * d9 - d10 * d10

	if d15 < 0:
		d0 = 0
	else:
		d15 = d15 * d15
		d0 = d15 * d15 * dot(grad3[k1], d9, d10)

	d16 = 0.5 - d11 * d11 - d12 * d12

	if d16 < 0:
		d1 = 0
	else:
		d16 = d16 * d16
		d1 = d16 * d16 * dot(grad3[l1], d11, d12)

	d17 = 0.5 - d13 * d13 - d14 * d14

	if d17 < 0:
		d2 = 0
	else:
		d17 = d17 * d17
		d2 = d17 * d17 * dot(grad3[i2], d13, d14)

	return 70 * (d0 + d1 + d2)


def get_island_height_value(p1, p2, p3, p4):

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

			if k * k + l * l > 4096 and noise_get_value(k, l) < -0.8999999761581421:
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


def is_island_chunk(p1, p2):

	return p1 * p1 + p2 * p2 > 4096 and get_island_height_value(p1, p2, 1, 1) >= 0


def set_random_seed(p1, p2, p3):

	i = p1 * 341873128712 + p2 * 132897987541 + world_seed + p3
	rand.setSeed(i)
	return rand


def can_spawn(chunk_x, chunk_z):

	i = chunk_x
	j = chunk_z

	if chunk_x < 0:
		chunk_x -= 19

	if chunk_z < 0:
		chunk_z -= 19

	k = int(chunk_x / 20)
	l = int(chunk_z / 20)
	random = set_random_seed(k, l, 10387313)
	k = k * 20
	l = l * 20
	k = k + int((random.nextInt(9) + random.nextInt(9)) / 2)
	l = l + int((random.nextInt(9) + random.nextInt(9)) / 2)

	return i == k and j == l and is_island_chunk(i, j)


if __name__ == '__main__':

	coords = [(x * 16, z * 16) for x, z in product(range(-650, 650), range(-650, 650)) if can_spawn(x, z)]
	print(json.dumps(coords))
