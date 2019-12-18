import java.util.Map;
import java.util.Map.Entry;

public class WorldInfo
{
    public long randomSeed;

    public WorldInfo(long seed)
    {
		this.randomSeed = seed;
    }

    /**
     * Returns the seed of current world.
     */
    public long getSeed()
    {
        return this.randomSeed;
    }
}
