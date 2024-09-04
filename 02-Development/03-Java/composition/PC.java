package coding.exercises.Section7.OOP.composition;

public class PC {
    private Case theCase;
    private Monitor monitor;
    private Motherboard motherboard;

    public PC(Case theCase, Monitor monitor, Motherboard motherboard) {
        this.theCase = theCase;
        this.monitor = monitor;
        this.motherboard = motherboard;
    }

    public void powerUp(){
        // getTheCase().pressPowerButton(); replaced by line below as removed getters
        theCase.pressPowerButton();
        drawLogo();
    }

    private void drawLogo(){
        // fancy graphics
        // getMonitor().drawPixel(1200,50,"yellow"); replaced by line below
        monitor.drawPixel(1200,50,"yellow");
    }

    // as we can access them directly as above you can remove getters as not needed
    /*
    private Case getTheCase() {
        return theCase;
    } */

    public Monitor getMonitor() {
        return monitor;
    }

    public Motherboard getMotherboard() {
        return motherboard;
    }

}
