public enum Rotation
{
    NONE("rotate_0"),
    CLOCKWISE_90("rotate_90"),
    CLOCKWISE_180("rotate_180"),
    COUNTERCLOCKWISE_90("rotate_270");

    public final String name;
    public static final String[] rotationNames = new String[values().length];

    private Rotation(String nameIn)
    {
        this.name = nameIn;
    }

    static {
        int i = 0;

        for (Rotation rotation : values())
        {
            rotationNames[i++] = rotation.name;
        }
    }
}
