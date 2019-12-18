import java.util.Calendar;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.Random;
import java.util.UUID;

public class World
{
    /** RNG for World. */
    public final Random rand = new Random();

    /**
     * holds information about a world (size on disk, time, spawn point, seed, ...)
     */
    public WorldInfo worldInfo;

    public World(WorldInfo info)
    {
        this.worldInfo = info;
    }

    /**
     * puts the World Random seed to a specific state dependant on the inputs
     */
    public Random setRandomSeed(int p_72843_1_, int p_72843_2_, int p_72843_3_)
    {
        long i = (long)p_72843_1_ * 341873128712L + (long)p_72843_2_ * 132897987541L + this.getWorldInfo().getSeed() + (long)p_72843_3_;
        this.rand.setSeed(i);
        return this.rand;
    }

	public WorldInfo getWorldInfo()
	{
		return this.worldInfo;
	}
}
