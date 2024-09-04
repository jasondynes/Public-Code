package coding.exercises;

public class PrimeNumbers {
    public static void main(String[] args) {
        //System.out.println(isPrime(1));
/*        for(int i = 0; i <100; i++){
            boolean prime = isPrime(i);
            if (prime){
                System.out.println(i + " is a Prime Number");
            } else {
                System.out.println(i + " is NOT a Prime Number");
            }
        }*/
        int count =0;
        for(int i = 0; i <3; i++){
            boolean prime = isPrime(i);
            if (prime){
                System.out.println(i + " is a Prime Number");
                count ++;
                if (count == 3){
                    break;
                }
            } else {
                System.out.println(i + " is NOT a Prime Number");
            }
        }
        System.out.println("Number of Prime Numbers found is " + count);

    }
    public static boolean isPrime(int n){
        if(n == 1){
            return false;
        }
        for(int i=2; i <= n/2; i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }
}
