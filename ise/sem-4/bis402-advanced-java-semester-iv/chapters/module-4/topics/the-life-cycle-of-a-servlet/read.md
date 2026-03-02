java
public class MyServlet extends HttpServlet {
    private Connection dbConnection;

    public void init() throws ServletException {
        // Initialize the database connection (pseudo-code)
        dbConnection = DriverManager.getConnection(...);
    }
}