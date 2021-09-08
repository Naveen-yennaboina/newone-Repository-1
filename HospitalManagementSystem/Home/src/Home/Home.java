package Home;
import Health.Health;
import Job.Job;


import java.util.Scanner;

public class Home
{
    public static void main(String[] args) {
        System.out.println("\n|***************************************************************************************************|");
        System.out.println("|*                                                                                                 *|");
        System.out.println("|*     ***-------****----*----**--      WELCOME NEW HOSPITAL       --**----*----****--------***    *|");
        System.out.println("|*                                                                                                 *|");
        System.out.println("|***************************************************************************************************|");
        while (true)
        {
            System.out.println("\n-------------***--------------->  HOME  <---------------***-----------\n");
            System.out.println("Enter - 1 - for Health purpose \n");
            System.out.println("Enter - 2 - for Enquiry purpose \n");
            System.out.println("Enter - 3 - for Job purpose \n");
            System.out.println("Enter - 4 - for Exit\n");
            System.out.println("------------**-----------**----------**-----------**----------**---------\n");
            Scanner scan = new Scanner(System.in);
            System.out.print("Enter your option                 : ");
            String s1 = scan.next();
            if(s1.equals("1"))
            {
                Health h = new Health();
                h.register();
            }
            else if (s1.equals("2"))
            {
                Enquiry e = new Enquiry();
                e.enquiry();
            }
            else if(s1.equals("3"))
            {
                Job j = new Job();
                j.job();
            }
            else if(s1.equals("4"))
            {
                System.out.println("THANK YOU, HAVE A NICE DAY");
                System.exit(0);
            }
            else
            {
                System.out.println("invalid input");
            }
        }
    }
}

