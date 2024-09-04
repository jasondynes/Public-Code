package coding.exercises;

public class SumOddRange {
    public static void main(String[] args) {
        System.out.println(sumOdd(1, 100));
        System.out.println(sumOdd(-1, 100));
        System.out.println(sumOdd(100, 100));
        System.out.println(sumOdd(13, 13));
        System.out.println(sumOdd(100, -100));
        System.out.println(sumOdd(100, 1000));

    }

    public static boolean isOdd(int number) {
        if (number == 0) {
            return false;
        } else if (number % 2 == 1) {
            return true;
        } else {
            return false;
        }
    }
    public static int sumOdd(int start, int end){
        if (start < 1 || end < 1 || end < start){
            return -1;
        }
        int sum = 0;
        for(int i=start; i <= end; i++){
            if(isOdd(i)) {
                sum = sum + i;
            }
        }
        return sum;
    }
}
