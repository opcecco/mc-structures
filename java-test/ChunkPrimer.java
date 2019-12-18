public class ChunkPrimer
{
    public static final int DEFAULT_STATE = 0;
    public final int[] data = new int[65536];

    public int getBlockState(int x, int y, int z)
    {
        int iblockstate = this.data[getBlockIndex(x, y, z)];
        return iblockstate == 0 ? DEFAULT_STATE : iblockstate;
    }

    public void setBlockState(int x, int y, int z, int state)
    {
        this.data[getBlockIndex(x, y, z)] = state;
    }

    public static int getBlockIndex(int x, int y, int z)
    {
        return x << 12 | z << 8 | y;
    }

    /**
     * Counting down from the highest block in the sky, find the first non-air block for the given location
     * (actually, looks like mostly checks x, z+1? And actually checks only the very top sky block of actual x, z)
     */
    public int findGroundBlockIdx(int x, int z)
    {
        int i = (x << 12 | z << 8) + 256 - 1;

        for (int j = 255; j >= 0; --j)
        {
            int iblockstate = this.data[i + j];

            if (iblockstate != 0 && iblockstate != DEFAULT_STATE)
            {
                return j;
            }
        }

        return 0;
    }
}
