import java.sql.*;

public class SecurityTest {
    public void vulnerableMethod(String userInput) throws Exception {
        // SQL Injection
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/test", "user", "pass");
        Statement stmt = conn.createStatement();
        stmt.execute("SELECT * FROM users WHERE name = '" + userInput + "'");
    }
}
