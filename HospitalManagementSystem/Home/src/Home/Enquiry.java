package Home;

import java.sql.*;
import java.util.Scanner;

public class Enquiry
{
    Statement stat = null;
    public void enquiry()
    {
        String url = "jdbc:mysql://localhost:3306/hospital_management_system";
        String user = "root";
        String pass = "naveen";
        try {
            Connection conn = DriverManager.getConnection(url, user, pass);
            stat = conn.createStatement();
        }
        catch (SQLException e)
        {
            System.out.println("something went wrong");
        }
        for(int i = 0; i<= 10; i++) {
            System.out.println("\n***-------------****----> Enquiry Portal <----****-------------***");
            System.out.println("enter 1 for Patient Enquiry ");
            System.out.println("enter 2 for Hospital Timings");
            System.out.println("enter 3 for Doctor List");
            System.out.println("enter 4 for Job Opportunities");
            System.out.println("enter 5 for Feedback");
            System.out.println("enter 6 for Home-Page");
            System.out.println("***-------------****----------******-----------****-------------***");
            Scanner scan = new Scanner(System.in);
            System.out.print("enter your Option                 : ");
            String opt = scan.next();
            if(opt.equals("1"))
                {
                    System.out.println("************************************************************************************");
                    System.out.print("enter patient name                : ");
                    String name = scan.next();
                    System.out.print("\nenter phone_number              : ");
                    long ph_num = scan.nextLong();
                    try {
                        ResultSet rs = stat.executeQuery("select * from patient_table where ph_num = " + ph_num + ", name = " + name);
                        while (rs.next()) {
                            System.out.println("---------------------------Patient Details------------------------------");
                            System.out.println("name              : " + rs.getString("name"));
                            System.out.println("phone             : " + rs.getString("phone"));
                            System.out.println("problem           : " + rs.getString("problem"));
                            System.out.println("join date         : " + rs.getString("join_date"));
                            System.out.println("consulting doctor : " + rs.getString("consulting_doctor"));
                            System.out.println("************************************************************************************");
                        }
                    } catch (SQLException e) {
                        System.out.println("Something went wrong");
                    }
                }
            else if(opt.equals("2"))
                {
                    System.out.println("\n************************************************************************************");
                    System.out.println("Hospital Timings.....");
                    System.out.println("Monday to Saturday..");
                    System.out.println("Morning : 9:30 AM     to     Night : 9:30 PM ");
                    System.out.println("************************************************************************************\n");
                }
            else if(opt.equals("3"))
                {
                    try {
                        System.out.println("\n************************************************************************************");
                        ResultSet rs = stat.executeQuery("select name, specialist from doctor_data ");
                        int i1 = 1;
                        while (rs.next()) {
                            System.out.println("Doctor No : "+i1);
                            System.out.println("           Name           =  "+rs.getString("name"));
                            System.out.println("           Specilization  =  "+rs.getString("specialist"));
                            i1 = i1+1;
                        }
                        System.out.println("************************************************************************************");
                    } catch (SQLException e) {
                        System.out.println("Something went wrong");
                        System.out.println(e);
                    }
                }
            else if(opt.equals("4"))
                {
                    System.out.println("presently there is no Opportunity");
                }
            else if(opt.equals("5"))
                {
                    System.out.println("\n************************************************************************************");
                    System.out.print("enter feedback                    : ");
                    String s1 = scan.next();
                    if (!s1.equals("")) {
                        System.out.println("Thank you for your feedback");
                    }
                    System.out.println("************************************************************************************");
                }
            else if(opt.equals("6"))
                {
                    System.out.println("************************************************************************************\n");
                    break;
                }
            }
    }
}

