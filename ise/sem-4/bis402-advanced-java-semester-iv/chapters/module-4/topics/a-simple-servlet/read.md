java
import javax.servlet.*;
import java.io.*;

public class SimpleServlet extends HttpServlet {
    @Override
    public void init() throws ServletException {
        // Initialize the Servlet
    }

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Handle GET requests
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h1>Hello World!</h1>");
    }

    @Override
    public void destroy() {
        // Destroy the Servlet
    }
}