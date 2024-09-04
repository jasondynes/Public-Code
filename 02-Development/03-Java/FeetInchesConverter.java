package coding.exercises;

/*public class FeetInchesConverter {
    public static double calcFeetAndInchesToCentimeters(double feet, double inches){
        if((feet >= 0) && (inches >=0 && inches <=12)){
            return (((feet * 12) + inches) * 2.54);
        } else {
            return -1;
        }
    }
    public static double calcFeetAndInchesToCentimeters(double inches){
        if(inches >= 0){
            return (inches * 2.54);
        } else {
            return -1;
        }
    }
}*/

public class FeetInchesConverter {
    public static double calcFeetAndInchesToCentimeters(double feet, double inches){
        if((feet >= 0) && (inches >=0 && inches <=12)){
            //return (((feet * 12) + inches) * 2.54);
            double centimetres = (((feet * 12) + inches) * 2.54);
            System.out.println(feet + " feet and " + inches + " inches = " + centimetres + " centimetres");
            return centimetres;
        } else {
            return -1;
        }
    }
    public static double calcFeetAndInchesToCentimeters(double inches){
        if(inches >= 0){
            double centimetres = (inches * 2.54);
            int feet = (int) inches / 12;
            double remainingInches = inches % 12;
            System.out.println(feet + " feet and " + remainingInches + " inches = " + centimetres + " centimetres");
            //System.out.println(inches);
            return centimetres;
        } else {
            return -1;
        }
    }
}