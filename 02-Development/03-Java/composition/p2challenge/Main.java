package coding.exercises.Section7.OOP.composition.p2challenge;

public class Main {
    public static void main(String[] args) {
        // instantiate room objects composing room object
        RoomDoor door = new RoomDoor(100, 200, 50, "wood", "red", "straight");
        RoomSofa sofa = new RoomSofa(200, 100, 100, "leather", "red");
        RoomWall wall1 = new RoomWall(220, 500, "white", "plasterboard");
        RoomWall wall2 = new RoomWall(220, 250, "red", "plasterboard");
        RoomWall wall3 = new RoomWall(220, 500, "blue", "plasterboard");
        RoomWall wall4 = new RoomWall(220, 250, "white", "plasterboard");
        RoomWindow window = new RoomWindow(120, 100, "sash", "white", false);

        //instantiate room object from above objects
        Room room = new Room(wall1, wall2, wall3, wall4, door, sofa, window);

        System.out.println("\nGet each wall separately using Wall getter\n");
        System.out.println(room.getWall1().getColour());
        System.out.println(room.getWall2().getColour());
        System.out.println(room.getWall3().getColour());
        System.out.println(room.getWall4().getColour());
        System.out.println("\nGet all wall colours using a method in Room class\n");
        room.getWallColours();

        System.out.println("\ncalls openWindow method in window class\n");
        window.openWindow();
        System.out.println("\ncalls method in Room class that opens room windows\n");
        room.openRoomWindow();;
        window.closeWindow();


    }
}
