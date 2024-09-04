package coding.exercises;

public class SharedDigit {
    public static void main(String[] args) {
        System.out.println(hasSharedDigit(12, 23));
        System.out.println(hasSharedDigit(9, 99));
        System.out.println(hasSharedDigit(15, 55));
        System.out.println(hasSharedDigit(12, 43));
        System.out.println(hasSharedDigit(12, 13));
    }

    public static boolean hasSharedDigit(int num1, int num2) {
        if ((num1 < 10) || (num1 > 99) || (num2 < 10) || (num2 > 99)) {
            return false;
        }
        int lastNum1 = num1 % 10;
        int firstNum1 = num1 / 10;
        int lastNum2 = num2 % 10;
        int firstNum2 = num2 / 10;

        return (lastNum1 == firstNum2 || lastNum1 == lastNum2 || firstNum1 == firstNum2 || firstNum1 == lastNum2);
    }
}

