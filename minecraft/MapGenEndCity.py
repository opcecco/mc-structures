from javarandom import Random

from .Rotation import Rotation
from .ChunkPrimer import ChunkPrimer


class MapGenEndCity:

	def __init__(self, p1):

		self.endProvider = p1
		self.worldObj = p1.worldObj


	def canSpawnStructureAtCoords(self, chunkX, chunkZ):

		i = chunkX
		j = chunkZ

		if chunkX < 0:
			chunkX -= 19

		if chunkZ < 0:
			chunkZ -= 19

		k = int(chunkX / 20)
		l = int(chunkZ / 20)
		random = self.worldObj.setRandomSeed(k, l, 10387313)
		k = k * 20
		l = l * 20
		k = k + int((random.nextInt(9) + random.nextInt(9)) / 2)
		l = l + int((random.nextInt(9) + random.nextInt(9)) / 2)

		if i == k and j == l and self.endProvider.isIslandChunk(i, j):
			i1 = self.funcb(i, j, self.endProvider)
			return i1 >= 60
		else:
			return False


	def funcb(self, p0, p1, p2):

		random = Random(p0 + p1 * 10387313)
		rotation = Rotation(random.nextInt(len(Rotation)))
		chunkprimer = ChunkPrimer()
		p2.setBlocksInChunk(p0, p1, chunkprimer)
		i = 5
		j = 5

		if rotation == Rotation.CLOCKWISE_90:
			i = -5
		elif rotation == Rotation.CLOCKWISE_180:
			i = -5
			j = -5
		elif rotation == Rotation.COUNTERCLOCKWISE_90:
			j = -5

		k = chunkprimer.findGroundBlockIdx(7, 7)
		l = chunkprimer.findGroundBlockIdx(7, 7 + j)
		i1 = chunkprimer.findGroundBlockIdx(7 + i, 7)
		j1 = chunkprimer.findGroundBlockIdx(7 + i, 7 + j)
		k1 = min(min(k, l), min(i1, j1))
		return k1
