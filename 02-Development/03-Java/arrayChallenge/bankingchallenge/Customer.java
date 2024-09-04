package coding.exercises.Section8arraysLists.arrayChallenge.bankingchallenge;

import java.util.ArrayList;

public class Customer {
    private String name;
    private ArrayList<Double> transactions;

    public Customer(String customerName, double initialAmount) {
        this.name = customerName;
        this.transactions = new ArrayList<Double>();
        addTransaction((initialAmount));
    }

    public String getName() {
        return name;
    }

    public ArrayList<Double> getTransactions() {
        return transactions;
    }

    public void addTransaction(double transaction){
        this.transactions.add(transaction);
    }
}

