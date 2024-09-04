package coding.exercises.Section7.OOP.encapsulation.challenge1;

public class Main {
    public static void main(String[] args) {
        Printer printer = new Printer(25, true);

        printer.printerInfo();
        System.out.println("\n");

        // print 10 pages
        int pagesPrinted = printer.printPage(10);
        printer.printerInfo();
        System.out.println("Pages printed was " + pagesPrinted + " new print count for Printer = " + printer.getNumberPagesPrinted() + "\n");

        // print 5 pages
        pagesPrinted = printer.printPage(5);
        printer.printerInfo();
        System.out.println("Pages printed was " + pagesPrinted + " new print count for Printer = " + printer.getNumberPagesPrinted() + "\n");

        // fill toner
        int tonerLevel = printer.fillToner(25);
        printer.printerInfo();
    }
}
