public class PrimitiveChallenge {
    public static void main(String[] args){
        byte myByteVariable = 10;
        short myShortVariable = 20;
        int myIntVariable = 50;
        long myLongVariable = 50000 + (10 * (myByteVariable + myShortVariable + myIntVariable));
        System.out.println("myLongVariable is " + myLongVariable);

    }

}
