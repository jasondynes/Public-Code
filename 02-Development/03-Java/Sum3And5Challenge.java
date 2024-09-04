package coding.exercises;

public class Sum3And5Challenge {
    public static void main(String[] args) {
        int sum = 0;
        int numSums =0;
        for(int i = 1; i <= 1000; i++){
            if ((i % 3 == 0) && (i % 5 == 0)){
                System.out.println("Number = " + i);
                sum = sum + i;
                numSums++;
                if (numSums == 5) break;
            }
        }
        System.out.println("Sum = " + sum );
    }
}
