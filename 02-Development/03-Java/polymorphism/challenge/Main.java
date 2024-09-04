package coding.exercises.Section7.OOP.polymorphism.challenge;

class Car {
    private String name;
    private int wheels;
    private int cylinders;
    private boolean engine;

    public Car(String name, int cylinders) {
        this.name = name;
        this.wheels = 4;
        this.cylinders = cylinders;
        this.engine = true;
    }

    public String getName() {
        return name;
    }

    //set to 4 by constructor so not needed
    public int getWheels() {
        return wheels;
    }

    public int getCylinders() {
        return cylinders;
    }
//not needed as set by constructor
    public boolean isEngine() {
        return engine;
    }

    public String startEngine(){
        return "Engine has been started....";
    }

    public String accelerate(){
        return "Car is accelerating....";
    }

    public String brake(){
        return "Car is braking....";
    }
}

class Vauxhall extends Car{
    public Vauxhall(String name, int cylinders) {
        super(name, cylinders);
    }

    @Override
    public String startEngine(){
        return "Vauxhall Engine has been started....";
    }

    @Override
    public String accelerate(){
        return "Vauxhall is accelerating....";
    }

    @Override
    public String brake(){
        return "Vauxhall is braking....";
    }
}

class Bentley extends Car {
    public Bentley(String name, int cylinders) {
        super(name, cylinders);
    }

    @Override
    public String startEngine(){
        // code to return class name instead of hard coding **********
        return getClass().getSimpleName() + " Engine has been started....";
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car("Ford", 6);
        System.out.println(car.startEngine());
        System.out.println(car.accelerate());;
        System.out.println(car.brake());

        Vauxhall car2 = new Vauxhall("Vauxhall", 4);
        System.out.println(car2.startEngine());
        System.out.println(car2.accelerate());;
        System.out.println(car2.brake());

        Bentley car3 = new Bentley("Bentley", 12);
        System.out.println(car3.startEngine());
        System.out.println(car3.accelerate());;
        System.out.println(car3.brake());
    }




}
