// note only byte, short, char and int data types can be used for a switch
// from Java 7 you can use strings in a switch

package coding.exercises;

public class SwitchChallenge {
    public static void main(String[] args) {
        char switchChar = 'A';
        String month = "January";

        switch (switchChar){
            case 'A': case 'B': case 'C': case 'D': case 'E':
                System.out.println("Found " + switchChar);
                break;
            default:
                System.out.println("Did not find A, B, C. D or E");
                break;
        }
        // remove case sensitivity
        switch (month.toLowerCase()){
            case "january":
                System.out.println("JAN");
                break;
            case "february":
                System.out.println("JAN");
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + month.toLowerCase());
        }
    }
}
