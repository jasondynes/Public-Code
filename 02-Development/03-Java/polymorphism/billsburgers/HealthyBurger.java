package coding.exercises.Section7.OOP.polymorphism.billsburgers;

public class HealthyBurger extends Hamburger{
    private String healthyExtra1Name;
    private double healthyExtra1Price;

    private String healthyExtra2Name;
    private double healthyExtra2Price;


    public HealthyBurger(String meat, double price) {
        super("Healthy", meat, price, "Brown Rye");
    }

    public void addHealthyAddition1(String healthyExtra1Name, double price){
        this.healthyExtra1Name = healthyExtra1Name;
        this.healthyExtra1Price = price;
    }

    public void addHealthyAddition2(String healthyExtra2Name, double price){
        this.healthyExtra2Name = healthyExtra2Name;
        this.healthyExtra2Price = price;
    }

    @Override
    public double itemizeHamburger() {
        double hamburgerPrice = super.itemizeHamburger();
        if(healthyExtra1Name != null){
            hamburgerPrice+=this.healthyExtra1Price;
            System.out.println("Added " + healthyExtra1Name + " for an extra " + healthyExtra1Price);
        }
        if(healthyExtra2Name != null){
            hamburgerPrice+=this.healthyExtra2Price;
            System.out.println("Added " + healthyExtra2Name + " for an extra " + healthyExtra2Price);
        }
        return hamburgerPrice;
    }
}
