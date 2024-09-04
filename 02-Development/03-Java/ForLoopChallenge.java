package coding.exercises;

public class ForLoopChallenge {

    public static void main(String[] args) {
        for(int i=2; i<9; i++){
            int amount = 10000;
            System.out.println(amount + " at " + i + "% interest = " + calculateInterest(amount, i));
            // to force to 2 decimal places used String.format below
            System.out.println(amount + " at " + i + "% interest = " + String.format("%.2f", calculateInterest(amount, i)));
        }

        for(int i=8; i>1; i--){
            int amount = 10000;
            System.out.println(amount + " at " + i + "% interest = " + calculateInterest(amount, i));
            // to force to 2 decimal places used String.format below
            System.out.println(amount + " at " + i + "% interest = " + String.format("%.2f", calculateInterest(amount, i)));
        }
    }

    public static double calculateInterest(double amount, double interestRate){
        return(amount *(interestRate/100));
    }
}
