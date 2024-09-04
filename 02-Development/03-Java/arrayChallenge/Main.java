package coding.exercises.Section8arraysLists.arrayChallenge;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // to read numbers from input
        int[] jasonArray = getIntegers(5);
        int [] sortedArray = sortIntegers(jasonArray);
        printArray(sortedArray);
    }
    public static int[] getIntegers(int arraySize){
    /*
        getIntegers has one parameter of type int which is the size of the array.
        It returns an array of entered integers from the keyboard.
     */
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter " + arraySize + " integer values.\r");
        int[] myArray = new int[arraySize];

        for(int i=0; i<myArray.length; i++){
            myArray[i] = scanner.nextInt();
        }
        return myArray;
    }

    public static void printArray(int[] array){
        /*
        printArray accepts an array and prints out the contents of the array. */

        for(int i=0; i<array.length; i++){
            System.out.println("Element " + i + " contents " + array[i]);
        }
    }

    public static int[] sortIntegers(int[] array){
    /*
        sortIntegers accepts the unsorted array. It should sort the array and return a new array containing the sorted numbers.
     */
        //Sort the array in ascending order using two for loops

        int[] sortedArray = Arrays.copyOf(array, array.length);

        boolean flag = true;
        int temp;
        while(flag) {
            flag = false;
            // element 0     160
            // element 1     50
            // element 2     40

            for(int i=0; i<sortedArray.length-1; i++) {
                if(sortedArray[i] < sortedArray[i+1]) {
                    temp = sortedArray[i];
                    sortedArray[i] = sortedArray[i+1];
                    sortedArray[i+1] = temp;
                    flag = true;
                }
            }
        }
        return sortedArray;
    }
}
