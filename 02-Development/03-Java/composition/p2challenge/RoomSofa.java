package coding.exercises.Section7.OOP.composition.p2challenge;

public class RoomSofa {
    private int width;
    private int depth;
    private int height;
    private String material;
    private String colour;

    public RoomSofa(int width, int depth, int height, String material, String colour) {
        this.width = width;
        this.depth = depth;
        this.height = height;
        this.material = material;
        this.colour = colour;
    }

    public int getWidth() {
        return width;
    }

    public int getDepth() {
        return depth;
    }

    public int getHeight() {
        return height;
    }

    public String getMaterial() {
        return material;
    }

    public String getColour() {
        return colour;
    }
}
