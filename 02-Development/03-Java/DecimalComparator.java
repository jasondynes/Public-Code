package coding.exercises;

/*Write a method areEqualByThreeDecimalPlaces with two parameters of type double.

        The method should return boolean and it needs to return true if two double numbers are the same up to three decimal places. Otherwise, return false.


        EXAMPLES OF INPUT/OUTPUT:

        * areEqualByThreeDecimalPlaces(-3.1756, -3.175); → should return true since numbers are equal up to 3 decimal places.

        * areEqualByThreeDecimalPlaces(3.175, 3.176); → should return false since numbers are not equal up to 3 decimal places

        * areEqualByThreeDecimalPlaces(3.0, 3.0); → should return true since numbers are equal up to 3 decimal places.

        * areEqualByThreeDecimalPlaces(-3.123, 3.123); → should return false since numbers are not equal up to 3 decimal places.


        TIP: Use paper and pencil.

        TIP: Use casting.

        NOTE: The areEqualByThreeDecimalPlaces method  needs to be defined as public static like we have been doing so far in the course.
        NOTE: Do not add a  main method to solution code.*/

public class DecimalComparator {
    public static boolean areEqualByThreeDecimalPlaces(double param1, double param2){
       int checkParam1 = (int) (param1 * 1000);
       int checkParam2 = (int) (param2 * 1000);

        if (checkParam1 == checkParam2){
            return true;
        }
        return false;
    }
}


/*
package com.TimBuchalka;

//Write a method areEqualByThreeDecimalPlaces with two parameters of type double.
//The method should return boolean and it needs to return true if two double numbers are the same up to three decimal places. Otherwise, return false.
//
//EXAMPLES OF INPUT/OUTPUT:
//* areEqualByThreeDecimalPlaces(-3.1756, -3.175); → should return true since numbers are equal up to 3 decimal places.
//* areEqualByThreeDecimalPlaces(3.175, 3.176); → should return false since numbers are not equal up to 3 decimal places
//* areEqualByThreeDecimalPlaces(3.0, 3.0); → should return true since numbers are equal up to 3 decimal places.
//* areEqualByThreeDecimalPlaces(-3.123, 3.123); → should return false since numbers are not equal up to 3 decimal places.

public class DecimalComparator {

    public static boolean areEqualByThreeDecimalPlaces(double one, double two) {
        int a = (int) one * 1000;
        int b = (int) two * 1000;

        if(a == b){
            System.out.println(true);
            return true;
        }
        else

            System.out.println(false);
        return false;
    }
}*/
