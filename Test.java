// Java test

import java.util.Random;


public class Test
{
	public static final double SQRT_3 = Math.sqrt(3.0D);
	public static final int[][] grad3 = new int[][] {{1, 1, 0}, { -1, 1, 0}, {1, -1, 0}, { -1, -1, 0}, {1, 0, 1}, { -1, 0, 1}, {1, 0, -1}, { -1, 0, -1}, {0, 1, 1}, {0, -1, 1}, {0, 1, -1}, {0, -1, -1}};

	public static final int[] noise_p = new int[512];

	public static long world_seed = -9026545427915476545L;
	public static Random rand = new Random();


	public static void initNoise()
	{
		rand.setSeed(world_seed);
		// Waste some time
		for (int i = 0; i < 66; ++i)
		{
			double dtrash;
			int itrash;

			dtrash = rand.nextDouble();
			dtrash = rand.nextDouble();
			dtrash = rand.nextDouble();

			for (int l = 0; l < 256; ++l)
			{
				itrash = rand.nextInt(256 - l) + l;
			}
		}

		double xo = rand.nextDouble() * 256.0D;
        double yo = rand.nextDouble() * 256.0D;
        double zo = rand.nextDouble() * 256.0D;

		for (int i = 0; i < 256; noise_p[i] = i++)
        {
            ;
        }

        for (int l = 0; l < 256; ++l)
        {
            int j = rand.nextInt(256 - l) + l;
            int k = noise_p[l];
            noise_p[l] = noise_p[j];
            noise_p[j] = k;
            noise_p[l + 256] = noise_p[l];
        }
	}


	public static long getSeed()
	{
		return world_seed;
	}


	public static Random setRandomSeed(int p_72843_1_, int p_72843_2_, int p_72843_3_)
    {
        long i = (long)p_72843_1_ * 341873128712L + (long)p_72843_2_ * 132897987541L + getSeed() + (long)p_72843_3_;
        rand.setSeed(i);
        return rand;
    }


	public static float sqrt(float value)
    {
        return (float)Math.sqrt((double)value);
    }
    public static float sqrt(double value)
    {
        return (float)Math.sqrt(value);
    }
	public static float abs(float value)
    {
        return value >= 0.0F ? value : -value;
    }
    public static int abs(int value)
    {
        return value >= 0 ? value : -value;
    }


	public static int fastFloor(double value)
    {
        return value > 0.0D ? (int)value : (int)value - 1;
    }
	private static double dot(int[] p_151604_0_, double p_151604_1_, double p_151604_3_)
    {
        return (double)p_151604_0_[0] * p_151604_1_ + (double)p_151604_0_[1] * p_151604_3_;
    }


	public static double noise_getValue(double p_151605_1_, double p_151605_3_)
    {
        double d3 = 0.5D * (SQRT_3 - 1.0D);
        double d4 = (p_151605_1_ + p_151605_3_) * d3;
        int i = fastFloor(p_151605_1_ + d4);
        int j = fastFloor(p_151605_3_ + d4);
        double d5 = (3.0D - SQRT_3) / 6.0D;
        double d6 = (double)(i + j) * d5;
        double d7 = (double)i - d6;
        double d8 = (double)j - d6;
        double d9 = p_151605_1_ - d7;
        double d10 = p_151605_3_ - d8;
        int k;
        int l;

        if (d9 > d10)
        {
            k = 1;
            l = 0;
        }
        else
        {
            k = 0;
            l = 1;
        }

        double d11 = d9 - (double)k + d5;
        double d12 = d10 - (double)l + d5;
        double d13 = d9 - 1.0D + 2.0D * d5;
        double d14 = d10 - 1.0D + 2.0D * d5;
        int i1 = i & 255;
        int j1 = j & 255;
        int k1 = noise_p[i1 + noise_p[j1]] % 12;
        int l1 = noise_p[i1 + k + noise_p[j1 + l]] % 12;
        int i2 = noise_p[i1 + 1 + noise_p[j1 + 1]] % 12;
        double d15 = 0.5D - d9 * d9 - d10 * d10;
        double d0;

        if (d15 < 0.0D)
        {
            d0 = 0.0D;
        }
        else
        {
            d15 = d15 * d15;
            d0 = d15 * d15 * dot(grad3[k1], d9, d10);
        }

        double d16 = 0.5D - d11 * d11 - d12 * d12;
        double d1;

        if (d16 < 0.0D)
        {
            d1 = 0.0D;
        }
        else
        {
            d16 = d16 * d16;
            d1 = d16 * d16 * dot(grad3[l1], d11, d12);
        }

        double d17 = 0.5D - d13 * d13 - d14 * d14;
        double d2;

        if (d17 < 0.0D)
        {
            d2 = 0.0D;
        }
        else
        {
            d17 = d17 * d17;
            d2 = d17 * d17 * dot(grad3[i2], d13, d14);
        }

        return 70.0D * (d0 + d1 + d2);
    }


	public static float getIslandHeightValue(int p_185960_1_, int p_185960_2_, int p_185960_3_, int p_185960_4_)
    {
        float f = (float)(p_185960_1_ * 2 + p_185960_3_);
        float f1 = (float)(p_185960_2_ * 2 + p_185960_4_);
        float f2 = 100.0F - sqrt(f * f + f1 * f1) * 8.0F;

        if (f2 > 80.0F)
        {
            f2 = 80.0F;
        }

        if (f2 < -100.0F)
        {
            f2 = -100.0F;
        }

        for (int i = -12; i <= 12; ++i)
        {
            for (int j = -12; j <= 12; ++j)
            {
                long k = (long)(p_185960_1_ + i);
                long l = (long)(p_185960_2_ + j);

                if (k * k + l * l > 4096L && noise_getValue((double)k, (double)l) < -0.8999999761581421D)
                {
                    float f3 = (abs((float)k) * 3439.0F + abs((float)l) * 147.0F) % 13.0F + 9.0F;
                    f = (float)(p_185960_3_ - i * 2);
                    f1 = (float)(p_185960_4_ - j * 2);
                    float f4 = 100.0F - sqrt(f * f + f1 * f1) * f3;

                    if (f4 > 80.0F)
                    {
                        f4 = 80.0F;
                    }

                    if (f4 < -100.0F)
                    {
                        f4 = -100.0F;
                    }

                    if (f4 > f2)
                    {
                        f2 = f4;
                    }
                }
            }
        }

		// System.out.println(f2);
        return f2;
    }


	public static boolean isIslandChunk(int p_185961_1_, int p_185961_2_)
    {
        return (long)p_185961_1_ * (long)p_185961_1_ + (long)p_185961_2_ * (long)p_185961_2_ > 4096L && getIslandHeightValue(p_185961_1_, p_185961_2_, 1, 1) >= 0.0F;
		// return true;
	}


	private static int func_191070_b(int p_191070_0_, int p_191070_1_)
    {
        rand.setSeed((long)(p_191070_0_ + p_191070_1_ * 10387313));
        int rotation = rand.nextInt(4);
        ChunkPrimer chunkprimer = new ChunkPrimer();
        setBlocksInChunk(p_191070_0_, p_191070_1_, chunkprimer);
        int i = 5;
        int j = 5;

        if (rotation == 1)
        {
            i = -5;
        }
        else if (rotation == 2)
        {
            i = -5;
            j = -5;
        }
        else if (rotation == 3)
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


	public static boolean canSpawnStructureAtCoords(int chunkX, int chunkZ)
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
        Random random = setRandomSeed(k, l, 10387313);
        k = k * 20;
        l = l * 20;
        k = k + (random.nextInt(9) + random.nextInt(9)) / 2;
        l = l + (random.nextInt(9) + random.nextInt(9)) / 2;

        if (i == k && j == l && isIslandChunk(i, j))
        {
            int i1 = func_191070_b(i, j, endProvider);
            return i1 >= 60;
			// return true;
        }
        else
        {
            return false;
        }
    }


	public static void main(String[] args)
	{
		initNoise();

		for (int x = -100; x < 100; ++x)
		{
			for (int z = -100; z < 100; ++z)
			{
				if (canSpawnStructureAtCoords(x, z))
					System.out.println("(" + x + ", " + z + ")");
			}
		}

		// int x = 562, z = -78;
		// System.out.println(canSpawnStructureAtCoords(x, z));

		return;
	}
}
