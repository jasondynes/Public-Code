package coding.exercises;

public class GreatestCommonDivisor {
    public static void main(String[] args) {
        System.out.println(getGreatestCommonDivisor(25, 15)); //5
        System.out.println(getGreatestCommonDivisor(12, 30)); //6
        System.out.println(getGreatestCommonDivisor(9, 18)); // -1
        System.out.println(getGreatestCommonDivisor(81, 153)); // 9
    }

    public static int getGreatestCommonDivisor(int first, int second){
        if (first < 10 || second < 10){
            return -1;
        }
        int commonDiv = 1;
        int highestDiv = 1;
        while(commonDiv <= first && commonDiv <= second){
            if (first % commonDiv == 0 && second % commonDiv == 0){
            highestDiv = commonDiv;
                //System.out.println(commonDiv);
            }
            commonDiv++;
        }
        return highestDiv;
    }
}
