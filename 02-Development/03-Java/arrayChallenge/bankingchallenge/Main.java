package coding.exercises.Section8arraysLists.arrayChallenge.bankingchallenge;

public class Main {

    public static void main(String[] args){
        Bank bank = new Bank("National Australia Bank");
        bank.addBranch("Adelaide");
        bank.addCustomer("Adelaide", "Tim", 50.05);
        bank.addCustomer("Adelaide", "Mike", 175.34);
        bank.addCustomer("Adelaide", "Percy", 220.12);

        bank.addBranch("Sydney");
        bank.addCustomer("Sydney", "Bob", 150.54);
        bank.addCustomerTransaction("Adelaide", "Tim", 44.22);
        bank.addCustomerTransaction("Adelaide", "Tim", 12.44);
        bank.addCustomerTransaction("Adelaide", "Mike", 1.65);
        bank.listCustomers("Adelaide", true);
        bank.listCustomers("Sydney", true);

        if(!bank.addBranch("Adelaide")){
            System.out.println("Adelaide branch already exists");
        }
        bank.addBranch("Melbourne");
        if(!bank.addCustomer("Melbourne", "Brian", 5.53)) {
            System.out.println("Error Melbourne branch does not exist");
        }
    }
}
