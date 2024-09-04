package coding.exercises.Section7.OOP.composition.p2challenge;

public class RoomDoor {
    private int width;
    private int height;
    private int depth;
    private String material;
    private String colour;
    private String handle;

    public RoomDoor(int width, int height, int depth, String material, String colour, String handle) {
        this.width = width;
        this.height = height;
        this.depth = depth;
        this.material = material;
        this.colour = colour;
        this.handle = handle;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public int getDepth() {
        return depth;
    }

    public String getMaterial() {
        return material;
    }

    public String getColour() {
        return colour;
    }

    public String getHandle() {
        return handle;
    }
}
