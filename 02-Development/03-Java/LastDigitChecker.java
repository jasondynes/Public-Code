package coding.exercises;

public class LastDigitChecker {
    public static void main(String[] args) {
        System.out.println(hasSameLastDigit(41, 22, 71)); //true
        System.out.println(hasSameLastDigit(23, 32, 42)); // true
        System.out.println(hasSameLastDigit(9, 99, 999)); // false
    }

    public static boolean hasSameLastDigit(int num1, int num2, int num3){
        System.out.println(num1 + " " + num2 + " " + num3);
        if (isValid(num1) && isValid(num2) && isValid(num3)){
            while (num1 > 9){
                num1 = num1 % 10;
            }

            while (num2 > 9){
                num2 = num2 % 10;
            }

            while (num3 > 9){
                num3 = num3 % 10;
            }

            if (num1 == num2 || num1 == num3 || num2 == num3){
                return true;
            }
        }
        return false;
    }

    public static boolean isValid(int num){
        if (num < 10 || num > 1000) {
            return false;
        }
        return true;
    }
}
