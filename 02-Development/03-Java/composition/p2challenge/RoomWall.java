package coding.exercises.Section7.OOP.composition.p2challenge;

public class RoomWall {
    private int height;
    private int width;
    private String colour;
    private String material;

    public RoomWall(int height, int width, String colour, String material) {
        this.height = height;
        this.width = width;
        this.colour = colour;
        this.material = material;
    }

    public int getHeight() {
        return height;
    }

    public int getWidth() {
        return width;
    }

    public String getColour() {
        return colour;
    }

    public String getMaterial() {
        return material;
    }
}
