package Java_learning;

import java.sql.SQLOutput;

public class Main {

    public static void main(String[] args) {
	// write your code here
        double myFirstDoubleNumber=20.00d;
        double mySecondDoubleNumber=80.00d;
        double total=100.00d*(myFirstDoubleNumber+mySecondDoubleNumber);
        System.out.println(total);
        double reminder=total % 40.00d;
        System.out.println(reminder);
        boolean reminderOk=(reminder==0) ? true : false;
        if(!reminderOk)
            System.out.println("Got some reminder!");
    }
}
