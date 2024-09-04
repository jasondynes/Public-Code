// note only byte, short, char and int data types can be used for a switch
// from Java 7 you can use strings in a switch
public class Switch {
    public static void main(String[] args) {
        Switch.getSwitchValue(1);
        Switch.getSwitchValue(2);
        Switch.getSwitchValue(10);

    }
    public static void getSwitchValue(int switchValue) {
        switch (switchValue) {
            case 1:
                System.out.println("Value was 1");
                break;
            case 2:
                System.out.println("Value was 2");
                break;
            default:
                System.out.println("Value was not 1 or 2 as it was " + switchValue);
                break;
        }
    }
}
