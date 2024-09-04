

public class ifThen {
    public static void main(String[] args){
        boolean isAlien = false;
        if (isAlien == false) {
            System.out.println("It is not an alien!");
            System.out.println("And I am scared of aliens!");
        }

        // tests if boolean is FALSE - more concise
        if (!isAlien) {
            System.out.println("It is not an alien!");
            System.out.println("And I am scared of aliens!");
        }

        // tests if boolean is TRUE - more concise
        if (isAlien) {
            System.out.println("It is not an alien!");
            System.out.println("And I am scared of aliens!");
        }

        int topScore = 100;
        if (topScore == 100) {
            System.out.println("You got the high score!");
        }
            topScore = 99;
        int secondTopScore = 60;
        if (topScore > secondTopScore && topScore < 100){
            System.out.println("Greater than second top score AND less than 100");
        }

        // tidier code for AND
        if ((topScore > secondTopScore) && (topScore < 100)){
            System.out.println("Greater than second top score AND less than 100");
        }

        // OR operator
        topScore = 100;
        secondTopScore = 60;
        if ((topScore > secondTopScore) || (topScore < 100)){
            System.out.println("Greater than second top score OR less than 100");
        }

        boolean isCar = false;
        if (isCar){
            System.out.println("This is not supposed to happen");
        }

        // ternary operator
        isCar = true;
        boolean wasCar = isCar ? true : false;
        System.out.println("wasCar: " + wasCar);
        System.out.println("isCar: " + isCar);

        if (wasCar){
            System.out.println("wasCar is true");
        } else {
            System.out.println("wasCar is false");
        }

        // ternary operator ?
        // Operand one is ageOfClient == 20
        // Operand two - TRUE here is the value to assign to the variable isEighteenOrOver if the condition above is TRUE

        int ageOfClient = 20;
        boolean isEighteenOrOver = (ageOfClient == 20) ? true : false;
    }
}

