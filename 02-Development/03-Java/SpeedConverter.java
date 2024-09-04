package coding.exercises;
// exercise 1

public class SpeedConverter {
    public static long toMilesPerHour(double kilometresPerHour){
        if (kilometresPerHour < 0){
            return -1;
        }
        else {
            long convertedMilesPerHour = Math.round(kilometresPerHour / 1.609d);
            return convertedMilesPerHour;
        }
    }

    public static void printConversion(double kilometersPerHour){
        if (kilometersPerHour < 0){
            System.out.println("Invalid Value");
        }
        else {
            double convertedMilesPerHour = toMilesPerHour(kilometersPerHour);
            System.out.println((double) kilometersPerHour + " km/h = " + (int) convertedMilesPerHour + " mi/h");
        }
    }
}

/*public class SpeedConverter {

    public static long toMilesPerHour(double kilometersPerHour) {

        if(kilometersPerHour < 0) {
            return -1;
        }

        return Math.round(kilometersPerHour / 1.609);
    }

    public static void printConversion(double kilometersPerHour) {

        if(kilometersPerHour <0) {
            System.out.println("Invalid Value");
        } else {
            long milesPerHour = toMilesPerHour(kilometersPerHour);
            System.out.println(kilometersPerHour +
                    " km/h= " + milesPerHour +
                    " mi/h");

        }
    }
}*/
