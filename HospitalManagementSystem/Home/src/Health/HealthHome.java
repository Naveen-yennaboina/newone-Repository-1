package Health;
import DBconnect.DBconnect;
import java.sql.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class HealthHome
{
    String name, ph_num, sex, prob;
    int age;
    public HealthHome(String name, int age, String ph_num, String sex,String prob)
    {
        this.name = name;
        this.age = age;
        this.ph_num = ph_num;
        this.sex = sex;
        this.prob = prob;
    }
    public void register()
    {
        String url = "jdbc:mysql://localhost:3306/hospital_management_system";
        String user = "root";
        String pass = "naveen";
        String q = "select name from doctor_data where specialist = '"+this.prob+"'";
        try
        {
            Connection connection = DriverManager.getConnection(url, user, pass);
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(q);
            String dr_name = "";
            String dr_name1 = "";
            int count = 0;
            while (resultSet.next()) {

                dr_name = resultSet.getString("name");
                dr_name1
                System.out.println(dr_name + " HE IS YOUR CONSULTING DOCTOR ");

            }
            Date date = new Date();
            SimpleDateFormat ft = new SimpleDateFormat("E dd.MM.yyyy 'at' hh:mm:ss a zzz");
            String q1 = "insert into patient_table(name, phone, problem, sex, ward, join_date, consulting_doctor)" +
                    "values('"+this.name+"', '"+this.ph_num+"', '"+this.prob+"', '"+this.sex+"', '"+102+"', '"+ft.format(date)
                    +"','"+dr_name+"')";
            DBconnect db = new DBconnect();
            db.insert(q1);
        }
        catch (SQLException e)
        {
            System.out.println("something went wrong.....");
            System.out.println(e);
        }

    }
}
