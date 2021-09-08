package Health;

import java.util.Scanner;

public class Health
{
    public void register()
    {
        System.out.println("***-------------****----> Enter Patient Details <----****-------------***");
        System.out.print("patient name                      : ");
        Scanner scanner = new Scanner(System.in);
        String name = scanner.next();
        System.out.print("\n"+"age                               : ");
        int age = scanner.nextInt();
        System.out.print("\n"+"Contact-number                    : ");
        String ph_num = scanner.next();
        System.out.print("\n"+"Gender                            : ");
        String sex = scanner.next();
        System.out.println("***-------------****----> Treatment Available <----****-------------***\n");
        System.out.println("enter 1 --->  Cardiologist       <------->     Heart Care");
        System.out.println("enter 2 --->  Oncologist         <------->     Cancer Care");
        System.out.println("enter 3 --->  ENT                <------->     Ear, Nose, Throat");
        System.out.println("enter 4 --->  Hematologist       <------->     Blood (Related)");
        System.out.println("enter 5 --->  Infection Disease  <------->     All(skin, viruses, malaria, parasites, HIV/AIDS)");
        System.out.println("enter 6 --->  Nephrologists      <------->     Kidney Care, High BP");
        System.out.println("enter 7 --->  Neurologist        <------->     Brain and Nervous System");
        System.out.println("enter 8 --->  Gynecologist       <------->     Women Health");
        System.out.println("enter 9 --->  Rheumatologist     <------->     Bones, Muscles, Joint-Pains etc... ");
        System.out.println("enter 10 -->  General Surgeon    <------->     Stomach, Liver, Appendix, Thyroid Gland, Gallbladder etc... \n");
        System.out.println("***-------------****-------------****---------------****-------------***");
        System.out.print("\n"+"Enter Problem                     : ");
        String opt = scanner.next();
        String prob = "";
        switch (opt) {
            case "1" -> prob = "cardiologist";
            case "2" -> prob = "oncologist";
            case "3" -> prob = "ent";
            case "4" -> prob = "hematologist";
            case "5" -> prob = "infection - disease";
            case "6" -> prob = "nephrologists";
            case "7" -> prob = "neurologist";
            case "8" -> prob = "gynecologist";
            case "9" -> prob = "rheumatologist";
            case "10"-> prob = "general-surgeon";
        }
        HealthHome hh = new HealthHome(name, age, ph_num, sex, prob);
        hh.register();
    }
}
