package coding.exercises;

public class NumberPalindrome {

    public static void main(String[] args) {
        System.out.println(isPalindrome(-1221) + " should be TRUE");
        System.out.println(isPalindrome(707) + " should be TRUE");
        System.out.println(isPalindrome(11212) + " should be FALSE");
        System.out.println(isPalindrome(1000) + " should be FALSE");

    }

    public static boolean isPalindrome(int number){
        // initial params
        String reverse = "";
        int lastDigit = 0;
        boolean palindrome = false;
        boolean negative = false;
        String originalNumber = Integer.toString(number);
        // is number negative?
        if (number < 0){
            negative = true;
        }

        // take number and keep dividing by 10 until number < 10 to get last digit
        // if number > 10 then divide int number by 10 to remove last digit
        // last digit becomes first digit of reverse number
        // make reverse number * 10
        // then repeat until

        // LOOP
        while (true){
            // remove last digit from number
            if (number >=10){
                // get last digit on number
                lastDigit = number % 10;
                // add last digit to reversed number
                reverse = reverse + lastDigit;
                number = number / 10;
            } else {
                reverse = reverse + number;
                break;
            }
        }
        if (originalNumber.equals(reverse)) {
            System.out.println("GO2");
            palindrome = true;
        }
        System.out.println("-------------");
        System.out.println("Original Number was " + originalNumber + " Reversed Number is " + reverse);
        return palindrome;
    }
}
