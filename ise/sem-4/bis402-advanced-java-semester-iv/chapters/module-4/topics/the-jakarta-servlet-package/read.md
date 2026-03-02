java
public class MyServlet extends HttpServlet {
    @Override
    public void init() throws ServletException {
        // Initialization code
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Handle GET requests
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Handle POST requests
    }

    @Override
    public void destroy() {
        // Destruction code
    }
}