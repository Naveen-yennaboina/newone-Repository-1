package Job;

import java.util.Scanner;

public class Job
{
    int count = 0;
    public void job() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("***-------------****----> Positions Available <----****-------------***\n");
        System.out.println("enter 1 --->  Cardiologist     ");
        System.out.println("enter 2 --->  Oncologist        ");
        System.out.println("enter 3 --->  ENT               ");
        System.out.println("enter 4 --->  Hematologist      ");
        System.out.println("enter 5 --->  Infection Disease  ");
        System.out.println("enter 6 --->  Nephrologists     ");
        System.out.println("enter 7 --->  Neurologist       ");
        System.out.println("enter 8 --->  Gynecologist      ");
        System.out.println("enter 9 --->  Rheumatologist   ");
        System.out.println("enter 10 -->  General Surgeon   \n");
        System.out.println("***-------------****-------------****---------------****-------------***");
        System.out.print("\n"+"Applying for                      : ");
        String opt = scanner.next();
        String position = "";
        switch (opt) {
            case "1" -> position = "cardiologist";
            case "2" -> position = "oncologist";
            case "3" -> position = "ent";
            case "4" -> position = "hematologist";
            case "5" -> position = "infection - disease";
            case "6" -> position = "nephrologists";
            case "7" -> position = "neurologist";
            case "8" -> position = "gynecologist";
            case "9" -> position = "rheumatologist";
            case "10"-> position = "general-surgeon";
        }
        System.out.println("***-------------****----> Enter Details <----****-------------***");
        System.out.print("\n"+"enter  name                       : ");
        String name = scanner.next();
        System.out.print("\n"+"enter age                         : ");
        int age = scanner.nextInt();
        System.out.print("\n"+"enter ph-number                   : ");
        String ph_num = scanner.next();
        System.out.print("\n"+"enter E-Mail                      : ");
        String email = scanner.next();
        if (!email.equals(""))
        {
            count = count + 5;
        }
        System.out.print("\n"+"enter project details             : ");
        String project = scanner.next();
        if (!project.equals(""))
        {
            count = count + 5;
        }
        Register register = new Register(position, name, age, ph_num, email, count);
        register.register();
    }
}
