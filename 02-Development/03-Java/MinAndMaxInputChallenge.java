package coding.exercises;

import java.util.Scanner;

public class MinAndMaxInputChallenge {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int minNum = 0;
        int maxNum = -0;
        boolean first = true;

        while(true){
            System.out.println("Enter number:");
            // checks that it qualifies as an int
            boolean isInt = scanner.hasNextInt();
            if(isInt){
                int numInput = scanner.nextInt();
                // handles first time set of min and max values
                if(first){
                    minNum = numInput;
                    maxNum = numInput;
                    first = false;
                }
                if(numInput < minNum){
                    minNum = numInput;
                }
                if(numInput > maxNum){
                    maxNum = numInput;
                }
            } else {
                System.out.println("Minimum Number is: " + minNum);
                System.out.println("Maximum number is: " + maxNum);
                scanner.close();
                break;
            }
            scanner.nextLine();
        }
    }
}

