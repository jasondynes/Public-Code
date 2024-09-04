package coding.exercises.Section7.OOP.encapsulation;

public class Main {

    public static void main(String[] args) {
            /*
        Player player = new Player();
        // IF PLAYER class variable names changed then below could fail or you forget to set as per below
        // can enforce a constructor with encapsulation so data needed is set and also within ranges you control
        player.name = "Tim";
        player.health = 20;
        player.weapon = "Sword";

        int damage = 10;
        player.loseHealth(damage);
        System.out.println("Remaining health = " + player.healthRemaining());

        damage = 11;
        // ****** BAD ENCAPSULATION as player class can be changed by line below in MAIN
        player.health = 200;
        player.loseHealth(damage);
        System.out.println("Remaining health = " + player.healthRemaining());
     */
        EnhancedPlayer player = new EnhancedPlayer("Tim", 50, "Sword");
        System.out.println("Remaining health = " + player.getHealth());
    }
}
