package DBconnect;

import java.sql.*;

public class DBconnect
{
    String url = "jdbc:mysql://localhost:3306/hospital_management_system";
    String user = "root";
    String pass = "naveen";
    Connection conn = null;
    Statement stat = null;
    public DBconnect() throws SQLException
    {
          this.conn = DriverManager.getConnection(url, user, pass);
          this.stat = this.conn.createStatement();
    }
    public void insert(String a)
    {
        try {
            this.stat.executeUpdate(a);
            System.out.println("process done!!!!....");
        }
        catch (SQLException e)
        {
            System.out.println("something went Wrong");
            e.printStackTrace();
        }
    }
    public void update()
    {

    }
    public void delete()
    {

    }
    public void read(String a)
    {
        try
        {
            ResultSet resultSet = this.stat.executeQuery(a);
            System.out.println("process done!!!!....");
        }
        catch (SQLException e)
        {
            System.out.println("something went Wrong");
            e.printStackTrace();
        }
    }
}
