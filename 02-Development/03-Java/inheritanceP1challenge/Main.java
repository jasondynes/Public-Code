package coding.exercises.Section7.OOP.inheritanceP1challenge;

public class Main {
    public static void main(String[] args) {
        Outlander outlander = new Outlander(36);
        outlander.steer(45);
        outlander.accelerate(30);
        outlander.steer(90);
        outlander.accelerate(-25);
        outlander.accelerate(-5);
    }
}
