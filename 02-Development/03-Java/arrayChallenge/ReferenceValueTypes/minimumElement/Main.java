package coding.exercises.Section8arraysLists.arrayChallenge.ReferenceValueTypes.minimumElement;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int numIntegers = readInteger();
        int[] myArray = readElements(numIntegers);
        int minNum = findMin(myArray);
        System.out.println("Minimum number in array is " + minNum);
    }

    private static int readInteger(){
        Scanner scanner = new Scanner(System.in);
        //System.out.println("Enter number of elements for user to enter\r");
        int elements = scanner.nextInt();
        return elements;
    }

    private static int[] readElements(int numberElements){
        int[] array = new int[numberElements];
        //System.out.println("Please enter " + numberElements + " elements");
        Scanner scanner = new Scanner(System.in);
        for(int i = 0; i < array.length; i++){
            array[i] = scanner.nextInt();
        }
        return array;
    }

    private static int findMin(int[] array){
        int minNum = array[0];
        for(int i=0; i<array.length; i++){
            if(minNum > array[i]){
                minNum = array[i];
            }
        }
        return minNum;
    }
}
