java
// Import necessary packages
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// Create a servlet to handle cookie creation and retrieval
public class CookieServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) {
        // Create a new cookie
        Cookie cookie = new Cookie("username", "johnDoe");
        cookie.setMaxAge(3600); // Set cookie expiration time to 1 hour

        // Add the cookie to the response header
        response.addCookie(cookie);

        // Retrieve the cookie from the request header
        Cookie[] cookies = request.getCookies();
        if (cookies != null) {
            for (Cookie c : cookies) {
                if (c.getName().equals("username")) {
                    System.out.println("Username: " + c.getValue());
                }
            }
        }
    }
}