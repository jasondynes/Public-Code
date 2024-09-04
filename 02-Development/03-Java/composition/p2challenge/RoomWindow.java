package coding.exercises.Section7.OOP.composition.p2challenge;

public class RoomWindow {
    private int width;
    private int height;
    private String style;
    private String colour;
    private Boolean open;

    public RoomWindow(int width, int height, String style, String colour, Boolean open) {
        this.width = width;
        this.height = height;
        this.style = style;
        this.colour = colour;
        this.open = false;
    }

    public void openWindow(){
        // set window to open
        open = true;
        System.out.println("Window is " + open);
    }

    public void closeWindow(){
        // set window to open
        open = false;
        System.out.println("Window is " + open);
    }

    /*
    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public String getStyle() {
        return style;
    }

    public String getColour() {
        return colour;
    }
     */
}
