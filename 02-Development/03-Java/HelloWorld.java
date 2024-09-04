public class HelloWorld {
    public static void main(String[] args){
        System.out.println("Hello Jason");

        int myFirstNumber = (10 + 5) + (2 * 10);
        int mySecondNumber = 12;
        int myThirdNumber = myFirstNumber * 2;
        int myTotal = myFirstNumber + mySecondNumber + myThirdNumber;
        int myLastOne = 1000 - myTotal;

        System.out.println("The numbers are " + myFirstNumber + ", " + mySecondNumber + " and " + myThirdNumber);
        System.out.println("My total is " + myTotal);
        System.out.println("My last one is " + myLastOne);

        // work out min and max value for a given data type
        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        System.out.println(Integer.MIN_VALUE);
        System.out.println("Integer min value is " + myMinIntValue);
        System.out.println("Integer max value is " + myMaxIntValue);
        // sout shortcut for system.out.println
    }
}
