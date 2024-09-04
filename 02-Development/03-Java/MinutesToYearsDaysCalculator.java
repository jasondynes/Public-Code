package coding.exercises;

public class MinutesToYearsDaysCalculator {
    public static void printYearsAndDays(long minutes){
        if (minutes < 0){
            System.out.println("Invalid Value");
        } else {
            int minsInDay = 60 * 24;
            int minsInYear =  365 * minsInDay;
            int calcDays = (int)((minutes % minsInYear) / minsInDay);
            int calcYears = (int) (minutes / minsInYear);
            System.out.println(minutes + " min = " + calcYears + " y and " + calcDays + " d");
        }
    }
}
