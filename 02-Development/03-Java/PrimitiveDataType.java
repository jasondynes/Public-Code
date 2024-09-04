public class PrimitiveDataType {
    public static void main(String[] args){
        // work out min and max value for a given data type
        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        System.out.println(Integer.MIN_VALUE);
        System.out.println("Integer min value is " + myMinIntValue);
        System.out.println("Integer max value is " + myMaxIntValue);
        System.out.println("Byte min value is " + Byte.MIN_VALUE);
        System.out.println("Byte max value is " + Byte.MAX_VALUE);
        System.out.println("Short min value is " + Short.MIN_VALUE);
        System.out.println("Short max value is " + Short.MAX_VALUE);
        System.out.println("Long min value is " + Long.MIN_VALUE);
        System.out.println("Long max value is " + Long.MAX_VALUE);
        long myLongValue = 2147483648L;
        System.out.println("Long is " + myLongValue);

        int myTotal = (myMinIntValue / 2);

        // casting as this will not work:    byte myNewByteValue = (myMinByteValue / 2);
        byte myMinByteValue = Byte.MIN_VALUE;
        byte myNewByteValue = (byte) (myMinByteValue / 2);
        short myMinShortValue = Short.MIN_VALUE;
        short myNewShortValue = (short) (myMinShortValue / 2);
    }
}
