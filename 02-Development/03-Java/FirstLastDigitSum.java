package coding.exercises;

public class FirstLastDigitSum {
    public static void main(String[] args) {
        System.out.println(sumFirstAndLastDigit(252));
        System.out.println(sumFirstAndLastDigit(257));
        System.out.println(sumFirstAndLastDigit(0));
        System.out.println(sumFirstAndLastDigit(5));
        System.out.println(sumFirstAndLastDigit(-10));
        System.out.println(sumFirstAndLastDigit(10));
            }
    public static int sumFirstAndLastDigit(int number){
        if (number < 0 ){
            return -1;
        }
        // get last digit of number

        int lastDigit = number % 10;
        // get first number
        while (number >= 10){
            number /= 10;
        }
        // return sum of last digit and first digit
        int finalSum = lastDigit + number;
        return finalSum;
    }
}
