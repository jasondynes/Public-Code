package coding.exercises.Section7.OOP.composition.p2challenge;

public class Room {
    private RoomWall wall1;
    private RoomWall wall2;
    private RoomWall wall3;
    private RoomWall wall4;
    private RoomDoor door;
    private RoomSofa sofa;
    private RoomWindow window;

    public Room(RoomWall wall1, RoomWall wall2, RoomWall wall3, RoomWall wall4, RoomDoor door, RoomSofa sofa, RoomWindow window) {
        this.wall1 = wall1;
        this.wall2 = wall2;
        this.wall3 = wall3;
        this.wall4 = wall4;
        this.door = door;
        this.sofa = sofa;
        this.window = window;
    }

    public void getWallColours(){
        System.out.println(wall1.getColour());
        System.out.println(wall2.getColour());
        System.out.println(wall3.getColour());
        System.out.println(wall4.getColour());
    }

    public void openRoomWindow(){
        System.out.println("Open room windows");
        window.openWindow();
    }

    public RoomWall getWall1() {
        return wall1;
    }

    public RoomWall getWall2() {
        return wall2;
    }

    public RoomWall getWall3() {
        return wall3;
    }

    public RoomWall getWall4() {
        return wall4;
    }

    public RoomDoor getDoor() {
        return door;
    }

    public RoomSofa getSofa() {
        return sofa;
    }

    public RoomWindow getWindow() {
        return window;
    }
}
