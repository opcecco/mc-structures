public class Main
{
	public static void main(String[] args)
	{
		long mySeed = -9026545427915476545L;

		World myWorld = new World(new WorldInfo(mySeed));
		ChunkGeneratorEnd myChunkGeneratorEnd = new ChunkGeneratorEnd(myWorld, mySeed);

		for (int x = -500; x < 500; ++x)
		{
			for (int z = -500; z < 500; ++z)
			{
				if (myChunkGeneratorEnd.endCityGen.canSpawnStructureAtCoords(x, z))
				{
					// System.out.println(x + "\t" + z);
					System.out.println((x * 16) + "\t" + (z * 16));
				}
			}
		}
	}
}
