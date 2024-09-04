package coding.exercises;

public class EvenNumber {
    public static void main(String[] args) {
        int number = 4;
        int finishNumber = 20;
        int evenCount = 0;
        while (number <= finishNumber){
            number++;
            if(!isEvenNumber(number)){
                continue;
            }
            System.out.println("Even number " + number);
            evenCount++;
            if(evenCount == 5){
                break;
            }
        }
        System.out.println("Total number of even numbers found is " + evenCount);
    }

    public static boolean isEvenNumber(int number){
        if (number % 2 == 0){
            return true;
        } else {
            return false;
        }
    }
}
