package coding.exercises.Section7.OOP.encapsulation.challenge1;

public class Printer {
    private int tonerLevel;
    private int numberPagesPrinted;
    private boolean duplex;

    public Printer(int tonerLevel, boolean duplex) {
        if(tonerLevel > -1 && tonerLevel <=100){
            this.tonerLevel = tonerLevel;
        } else {
            this.tonerLevel = -1;
        }
        this.duplex = duplex;
        this.numberPagesPrinted = 0;
    }

    public int fillToner(int amount){
        if(amount > 0 && amount <=100){
            if(this.tonerLevel + amount > 100){
                return -1;
            } else {
                System.out.println("\nAttempting to fill toner by " + amount + "%");
                tonerLevel = tonerLevel + amount;
                return this.tonerLevel;
            }
        } else {
            return -1;
        }
    }

    public int printPage(int pages){
        int pagesToPrint = pages;
        if(this.duplex){
            // to cope with odd number of pages and duplex you need below
            pagesToPrint = (pages / 2) + (pages % 2);
            System.out.println("Printing in Duplex mode");
        }
        System.out.println("Printer has printed " + pagesToPrint + " pages");
        this.numberPagesPrinted = numberPagesPrinted + pagesToPrint;
        return pagesToPrint;
    }

    public void printerInfo(){
        System.out.println("Toner level: " + tonerLevel);
        System.out.println("Pages printed: " + numberPagesPrinted);
        System.out.println("Duplex (True/False): " + duplex);
    }

    public int getTonerLevel() {
        return tonerLevel;
    }

    public int getNumberPagesPrinted() {
        return numberPagesPrinted;
    }

    public boolean isDuplex() {
        return duplex;
    }
}
