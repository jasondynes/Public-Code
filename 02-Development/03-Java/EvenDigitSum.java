package coding.exercises;

public class EvenDigitSum {
    public static void main(String[] args) {
        System.out.println(getEvenDigitSum(123456789));
        System.out.println(getEvenDigitSum(252));
        System.out.println(getEvenDigitSum(-22));
    }
    public static int getEvenDigitSum(int number){
        int lastDigit = 0;
        int evenSum = 0;

        if (number < 0){
            return -1;
        }
        while(number >= 10){
            //get last digit
            lastDigit = number % 10;
            if (lastDigit % 2 == 0){
                evenSum = evenSum + lastDigit;
            }
            number = number / 10;
        }
        if (number % 2 == 0){
            evenSum = evenSum + number;
        }
        return evenSum;
    }
}
