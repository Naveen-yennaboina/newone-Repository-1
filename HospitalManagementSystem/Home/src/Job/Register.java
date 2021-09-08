package Job;
import DBconnect.DBconnect;
import java.util.Scanner;

public class Register
{
    String dr_name, ph_num, email, position, college;
    int age, count, exp;
    public Register(String position, String name, int age, String ph_num, String email, int count)
    {
        this.dr_name = name;
        this.age = age;
        this.ph_num = ph_num;
        this.email = email;
        this.count = count;
        this.position = position;
    }
    public void register()
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("***-------------***----> enter Experience Details <----***-------------***");
        System.out.print("company name                      : ");
        String c_name = scanner.next();
        System.out.print("\n"+"Experience                        : ");
        exp = scanner.nextInt();
        if (exp != 0)
        {
            this.count = this.count + 5;
        }
        System.out.print("\n"+"Specialization                    : ");
        String position = scanner.next();
        if (!position.equals(" "))
        {
            this.count = this.count + 1;
        }
        System.out.println("***-------------***----> Hello "+this.dr_name+" enter Educational Details <----***-------------***");
        System.out.print("College Name                      : ");
        String col = scanner.next();
        college = col.replace(" ", "_");
        System.out.print("\n"+"enter degree                      : ");
        String degree = scanner.next();
        if (!degree.equals(""))
        {
            this.count = this.count + 1;
        }
        System.out.print("\n"+"enter CGPA or Percentage          : ");
        int cgpa = scanner.nextInt();
        if (cgpa != 0)
        {
            this.count = this.count + 1;
        }
        conform();
    }
    public void conform()
    {
        if (this.count == 18)
        {
            try {
                System.out.println("\nwe are processing your request.....\n");
                int salary = 25000;
                String quarry = "insert into doctor_data" + "(name, age, email, phone, specialist, experiance, college, patient_count)" + "values('"+this.dr_name+"','"
                        +this.age+"','"+this.email+"','"+this.ph_num+"','"+this.position +"','"+exp+"','"+college+"','"+0+"')";
                DBconnect db = new DBconnect();
                db.insert(quarry);
                System.out.println("***-------**--> your selected <--**-------*** ");
            } catch (Exception e)
            {
                System.out.println("something went wrong");
            }
        }
        else
        {
            System.out.println("Sorry your not selected");
            System.out.println("we hope you will got placed sooner");
        }
    }
}
