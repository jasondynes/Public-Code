package coding.exercises;

public class PerfectNumber {
    public static boolean isPerfectNumber(int number){
        if (number < 1){
            return false;
        }

        int counter = 1;
        int sumFactors = 0;
        while (counter < number) {
            if (number % counter == 0) {
                System.out.println(counter);
                sumFactors = sumFactors + counter;
                }
                counter++;
            }
        if (sumFactors == number){
            return true;
        }
        return false;
    }
}
