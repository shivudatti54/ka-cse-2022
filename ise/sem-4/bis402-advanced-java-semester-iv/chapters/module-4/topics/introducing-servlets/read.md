java
import javax.servlet.*;
import java.io.*;

public class HelloWorldServlet extends HttpServlet {
    @Override
    public void init() throws ServletException {
        System.out.println("Servlet initialized");
    }

    @Override
    public void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h1>Hello, World!</h1>");
    }

    @Override
    public void destroy() {
        System.out.println("Servlet destroyed");
    }
}