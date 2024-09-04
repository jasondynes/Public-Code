public class FloatDouble {
    public static void  main(String[] args){
        float myMinFloatValue = Float.MIN_VALUE;
        float myMaxFloatValue = Float.MAX_VALUE;
        System.out.println("Min Float value " + myMinFloatValue);
        System.out.println("Max Float value " + myMaxFloatValue);

        double myMinDoubleValue = Double.MIN_VALUE;
        double myMaxDoubleValue = Double.MAX_VALUE;
        System.out.println("Min Double value " + myMinDoubleValue);
        System.out.println("Max Double value " + myMaxDoubleValue);

        int myIntValue = 5 / 3;
        float myFloatValue = 5f / 3f;
        double myDoubleValue = 5d / 3d;

        System.out.println("My Int Value is " + myIntValue);
        System.out.println("My Float Value is " + myFloatValue);
        System.out.println("My Double Value is " + myDoubleValue);
    }
}
