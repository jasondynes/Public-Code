package coding.exercises.Section7.OOP.encapsulation.MainChallenge;

public class Printer {
    private int tonerLevel;
    private int pagesPrinted;
    private boolean duplex;

    public Printer(int tonerLevel, boolean duplex) {
        if(tonerLevel > -1 && tonerLevel <=100){
            this.tonerLevel = tonerLevel;
        } else {
            this.tonerLevel = -1;
        }
        this.duplex = duplex;
        this.pagesPrinted = 0;
    }

    public int addToner(int tonerAmount){
        if(tonerAmount > 0 && tonerAmount <=100){
            if(this.tonerLevel + tonerAmount > 100){
                return -1;
            } else {
                //System.out.println("\nAttempting to fill toner by " + tonerAmount + "%");
                tonerLevel = tonerLevel + tonerAmount;
                return this.tonerLevel;
            }
        } else {
            return -1;
        }
    }

    public int printPages(int pagesToPrint){
        //int pagesToPrint = pagesToPrint;
        if(this.duplex){
            // to cope with odd number of pages and duplex you need below
            pagesToPrint = (pagesToPrint / 2) + (pagesToPrint % 2);
            System.out.println("Printing in Duplex mode");
        }
        System.out.println("Printer has printed " + pagesToPrint + " pages");
        this.pagesPrinted = pagesPrinted + pagesToPrint;
        return pagesToPrint;
    }


    public int getPagesPrinted() {
        return pagesPrinted;
    }
}
