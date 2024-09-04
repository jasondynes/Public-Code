package coding.exercises;

public class Main {
    public static void main(String[] args) {
        System.out.println("\n*** Speed Converter tests ***");
        System.out.println(SpeedConverter.toMilesPerHour(1.5));
        System.out.println(SpeedConverter.toMilesPerHour(10.25));
        System.out.println(SpeedConverter.toMilesPerHour(-5.6));
        System.out.println(SpeedConverter.toMilesPerHour(25.42));
        System.out.println(SpeedConverter.toMilesPerHour(75.114));

        System.out.println("\n*** Megabytes converter tests ***");
        MegaBytesConverter.printMegaBytesAndKiloBytes(2500);
        MegaBytesConverter.printMegaBytesAndKiloBytes(-1024);
        MegaBytesConverter.printMegaBytesAndKiloBytes(5000);

        System.out.println("\n*** Barking Dog tests ***");
        System.out.println(BarkingDog.shouldWakeUp(true, 1));
        System.out.println(BarkingDog.shouldWakeUp(false, 2));
        System.out.println(BarkingDog.shouldWakeUp(true, 8));
        System.out.println(BarkingDog.shouldWakeUp(true, -1));

        System.out.println("\n*** Leap Year Calculator tests ***");
        System.out.println(LeapYear.isLeapYear(-1600));
        System.out.println(LeapYear.isLeapYear(1600));
        System.out.println(LeapYear.isLeapYear(2017));
        System.out.println(LeapYear.isLeapYear(2000));
        System.out.println(LeapYear.isLeapYear(1700));

        System.out.println("\n*** Decimal Comparator tests ***");
        System.out.println(DecimalComparator.areEqualByThreeDecimalPlaces(-3.1756, -3.175));
        System.out.println(DecimalComparator.areEqualByThreeDecimalPlaces(3.175, 3.176));
        System.out.println(DecimalComparator.areEqualByThreeDecimalPlaces(3.0, 3.0));
        System.out.println(DecimalComparator.areEqualByThreeDecimalPlaces(-3.123, 3.123));

        System.out.println("\n*** Equal Sum Checker tests ***");
        System.out.println(EqualSumChecker.hasEqualSum(1,1,1));
        System.out.println(EqualSumChecker.hasEqualSum(1,1,2));
        System.out.println(EqualSumChecker.hasEqualSum(1,-1,0));

        System.out.println("\n*** Teen Number Checker tests ***");
        System.out.println(TeenNumberChecker.hasTeen(9, 99, 19));
        System.out.println(TeenNumberChecker.hasTeen(23, 15, 42));
        System.out.println(TeenNumberChecker.hasTeen(22, 23, 24));
        System.out.println(TeenNumberChecker.isTeen(9));
        System.out.println(TeenNumberChecker.isTeen(13));

        System.out.println("\n*** Feet Inches converter tests ***");
        System.out.println(FeetInchesConverter.calcFeetAndInchesToCentimeters(6, 2.5));
        System.out.println(FeetInchesConverter.calcFeetAndInchesToCentimeters(13));

        System.out.println("\n*** Seconds and Minutes challenge tests ***");
        System.out.println(SecondsAndMinutes.getDurationString(59, 2));
        System.out.println(SecondsAndMinutes.getDurationString(3605));
        System.out.println(SecondsAndMinutes.getDurationString(3599));
        System.out.println(SecondsAndMinutes.getDurationString(65, 45));

        System.out.println("\n*** Are calculator tests ***");
        System.out.println(AreaCalculator.area(5.0));
        System.out.println(AreaCalculator.area(-1));
        System.out.println(AreaCalculator.area(5.0, 4.0));
        System.out.println(AreaCalculator.area(-1.0, 4.0));
        MinutesToYearsDaysCalculator.printYearsAndDays(525600);
        MinutesToYearsDaysCalculator.printYearsAndDays(1051200);
        MinutesToYearsDaysCalculator.printYearsAndDays(561600);
    }
}
