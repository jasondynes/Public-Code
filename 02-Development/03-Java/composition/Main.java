package coding.exercises.Section7.OOP.composition;

public class Main {
    public static void main(String[] args) {
        Dimensions dimensions = new Dimensions(20,20,5);
        Case theCase = new Case("220B", "DEll", "240", dimensions);
        Monitor theMonitor = new Monitor("27 inch Beast", "Acer", 27, new Resolution(2540,1440));
        Motherboard theMotherBoard = new Motherboard("BJ-200", "Asus", 4,6, "v2.44");

        // PC object made from 3 objects i.e. the case, monitor and motherboard
        PC thePC = new PC(theCase, theMonitor, theMotherBoard);

        // to use method drawPixel in monitor class on the monitor object for the PC
        thePC.getMonitor().drawPixel(1500, 1200,"red");


        //other examples of calling object methods composing the PC
        thePC.getMotherboard().loadProgram("Windows 1.0");

        // thePC.getTheCase().pressPowerButton(); replaced by line below after refactoring of
        thePC.powerUp();
    }
}
