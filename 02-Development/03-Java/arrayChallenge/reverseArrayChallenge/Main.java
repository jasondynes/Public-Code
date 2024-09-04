package coding.exercises.Section8arraysLists.arrayChallenge.reverseArrayChallenge;

import java.util.Arrays;

public class Main {

  public static void main(String[] args) {
      int[] originalArray = new int[]{4, 5, 6, 7, 8};
      reverse(originalArray);
  }

  private static void reverse(int[] arrayToReverse){
      System.out.println("Array = " + Arrays.toString(arrayToReverse));

      int[] tmpArray = new int[arrayToReverse.length];
      int counter = arrayToReverse.length -1;
      for(int i=0; i<arrayToReverse.length; i++){
          tmpArray[counter] = arrayToReverse[i];
          counter--;
      }
      System.out.println("Reversed array = " + Arrays.toString(tmpArray));
  }
}
