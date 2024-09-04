public class operatorChallenge {
    public static void main(String[] args) {
        double myDouble = 20.00d;
        double myDouble2 = 80.00d;
        double doubleCalc = 100.00d * (myDouble + myDouble2);
        double remainder = doubleCalc % 40.00d;
        boolean boolCheck = (remainder == 0) ? true : false;
        System.out.println("The result is " + boolCheck);
        if (boolCheck == false) {
            System.out.println("Got some remainder");
        }
    }
}

