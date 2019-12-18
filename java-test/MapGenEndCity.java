import java.util.Random;

public class MapGenEndCity
{
    public final ChunkGeneratorEnd endProvider;

    public MapGenEndCity(ChunkGeneratorEnd p_i46665_1_)
    {
        this.endProvider = p_i46665_1_;
    }

    public boolean canSpawnStructureAtCoords(int chunkX, int chunkZ)
    {
        int i = chunkX;
        int j = chunkZ;

        if (chunkX < 0)
        {
            chunkX -= 19;
        }

        if (chunkZ < 0)
        {
            chunkZ -= 19;
        }

        int k = chunkX / 20;
        int l = chunkZ / 20;
        Random random = this.endProvider.worldObj.setRandomSeed(k, l, 10387313);
        k = k * 20;
        l = l * 20;
        k = k + (random.nextInt(9) + random.nextInt(9)) / 2;
        l = l + (random.nextInt(9) + random.nextInt(9)) / 2;

        if (i == k && j == l && this.endProvider.isIslandChunk(i, j))
        {
            int i1 = func_191070_b(i, j, this.endProvider);
            return i1 >= 60;
        }
        else
        {
            return false;
        }
    }

    public static int func_191070_b(int p_191070_0_, int p_191070_1_, ChunkGeneratorEnd p_191070_2_)
    {
        Random random = new Random((long)(p_191070_0_ + p_191070_1_ * 10387313));
        Rotation rotation = Rotation.values()[random.nextInt(Rotation.values().length)];
        ChunkPrimer chunkprimer = new ChunkPrimer();
        p_191070_2_.setBlocksInChunk(p_191070_0_, p_191070_1_, chunkprimer);
        int i = 5;
        int j = 5;

        if (rotation == Rotation.CLOCKWISE_90)
        {
            i = -5;
        }
        else if (rotation == Rotation.CLOCKWISE_180)
        {
            i = -5;
            j = -5;
        }
        else if (rotation == Rotation.COUNTERCLOCKWISE_90)
        {
            j = -5;
        }

        int k = chunkprimer.findGroundBlockIdx(7, 7);
        int l = chunkprimer.findGroundBlockIdx(7, 7 + j);
        int i1 = chunkprimer.findGroundBlockIdx(7 + i, 7);
        int j1 = chunkprimer.findGroundBlockIdx(7 + i, 7 + j);
        int k1 = Math.min(Math.min(k, l), Math.min(i1, j1));
        return k1;
    }
}
