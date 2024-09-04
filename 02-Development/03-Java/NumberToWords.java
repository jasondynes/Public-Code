package coding.exercises;

public class NumberToWords {
    public static void main(String[] args) {
        numberToWords(123);
        System.out.printf("END%n");
        numberToWords(1010);
        System.out.printf("END%n");
        numberToWords(1000);
        System.out.printf("END%n");
        numberToWords(-12);
    }

    public static void numberToWords(int number){
        if(number < 0){
            System.out.println("Invalid Value");
        }
        else {
            int DigitCount = getDigitCount(number);
            int numberReverse = reverse(number);
            //int lastDigit = 0;
            for (int i = 0; i < DigitCount; i++) {
                int lastDigit = numberReverse % 10;
                numberReverse = numberReverse / 10;

                switch (lastDigit) {
                    case 0:
                        System.out.print("Zero ");
                        break;
                    case 1:
                        System.out.print("One ");
                        break;
                    case 2:
                        System.out.print("Two ");
                        break;
                    case 3:
                        System.out.print("Three ");
                        break;
                    case 4:
                        System.out.print("Four ");
                        break;
                    case 5:
                        System.out.print("Five ");
                        break;
                    case 6:
                        System.out.print("Six ");
                        break;
                    case 7:
                        System.out.print("Seven ");
                        break;
                    case 8:
                        System.out.print("Eight ");
                        break;
                    case 9:
                        System.out.print("Nine ");
                        break;
                }
            }
        }
    }

    public static int getDigitCount(int number) {
        if (number < 0) {
            return -1;
        }
        int count = 1;
        while (number > 9) {
            number = number / 10;
            count++;
        }
        return count;
    }

    public static int reverse(int number) {
        int reversedNumber = 0;
        int lastDigit = 0;
        while (number != 0) {
            lastDigit = number % 10;
            reversedNumber = reversedNumber * 10 + lastDigit;
            number /= 10;
        }
        return reversedNumber;
    }
}
