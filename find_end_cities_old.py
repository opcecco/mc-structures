#!/usr/bin/env python3

import sys
import json
from math import sqrt, floor
from pprint import pprint
from itertools import product
from javarandom import Random


SQRT_3 = sqrt(3)
grad3 = [[1, 1, 0], [ -1, 1, 0], [1, -1, 0], [ -1, -1, 0], [1, 0, 1], [ -1, 0, 1], [1, 0, -1], [ -1, 0, -1], [0, 1, 1], [0, -1, 1], [0, 1, -1], [0, -1, -1]]

island_noise_perms = [0] * 512
chunk = [False] * 65536
buffer = None

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
	island_noise_perms[i] = i

for l in range(256):
	j = rand.nextInt(256 - l) + l
	k = island_noise_perms[l]
	island_noise_perms[l] = island_noise_perms[j]
	island_noise_perms[j] = k
	island_noise_perms[l + 256] = island_noise_perms[l]


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
	k1 = island_noise_perms[i1 + island_noise_perms[j1]] % 12
	l1 = island_noise_perms[i1 + k + island_noise_perms[j1 + l]] % 12
	i2 = island_noise_perms[i1 + 1 + island_noise_perms[j1 + 1]] % 12
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


def get_heights(p2, p3, p4, p5, p6, p7):

	global buffer

	if not buffer:
		buffer = [0] * (p5 * p6 * p7)

	d0 = 684.412
	d1 = 684.412
	d0 = d0 * 2
	# Noise shit
	i = int(p2 / 2)
	j = int(p4 / 2)
	k = 0


def set_chunk_blocks(x, z):

	i = 2
	j = 3
	k = 33
	l = 3
	get_heights(x * 2, 0, z * 2, 3, 33, 3)

	for i1 in range(2):
		for j1 in range(2):
			for k1 in range(32):
				d0 = 0.25
				d1 = buffer[((i1 + 0) * 3 + j1 + 0) * 33 + k1 + 0]
				d2 = buffer[((i1 + 0) * 3 + j1 + 1) * 33 + k1 + 0]
				d3 = buffer[((i1 + 1) * 3 + j1 + 0) * 33 + k1 + 0]
				d4 = buffer[((i1 + 1) * 3 + j1 + 1) * 33 + k1 + 0]
				d5 = (buffer[((i1 + 0) * 3 + j1 + 0) * 33 + k1 + 1] - d1) * 0.25
				d6 = (buffer[((i1 + 0) * 3 + j1 + 1) * 33 + k1 + 1] - d2) * 0.25
				d7 = (buffer[((i1 + 1) * 3 + j1 + 0) * 33 + k1 + 1] - d3) * 0.25
				d8 = (buffer[((i1 + 1) * 3 + j1 + 1) * 33 + k1 + 1] - d4) * 0.25

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
							blockstate = False
							if d15 > 0:
								blockstate = True
							x = i2 + i1 * 8
							y = l1 + k1 * 4
							z = j2 + j1 * 8
							chunk[x << 12 | z << 8 | y] = blockstate
							d15 += d16

						d10 += d12
						d11 += d13

					d1 += d5
					d2 += d6
					d3 += d7
					d4 += d8


def find_ground_block(x, z):

	i = (x << 12 | z << 8) + 256 - 1

	for j in range(255, -1, -1):
		blockstate = chunk[i + j]

		if blockstate:
			return j

	return 0


def generation_block_height(p0, p1):

	rand.setSeed(p0 + p1 * 10387313)
	rotation = rand.nextInt(4)
	set_chunk_blocks(p0, p1)
	i = 5
	j = 5

	if rotation == 1:
		i = -5
	elif rotation == 2:
		i = -5
		j = -5
	elif rotation == 3:
		j = -5

	k = find_ground_block(7, 7)
	l = find_ground_block(7, 7 + j)
	i1 = find_ground_block(7 + i, 7)
	j1 = find_ground_block(7 + i, 7 + j)
	k1 = min(min(k, l), min(i1, j1))
	return k1


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

	return i == k and j == l and is_island_chunk(i, j) #and generation_block_height(i, j) >= 60


if __name__ == '__main__':

	# coords = [(x * 16, z * 16) for x, z in product(range(-100, 100), range(-100, 100)) if can_spawn(x, z)]
	# print(json.dumps(coords))

	coords = [(x, z) for x, z in product(range(-100, 100), range(-100, 100)) if can_spawn(x, z)]
	pprint(coords)
