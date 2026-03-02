java
// In a Servlet (or Scriptlet in JSP)
HttpSession session = request.getSession(true); // Gets existing or creates new session
session.setAttribute("username", "JohnDoe"); // Storing an object in session
session.setAttribute("cartItems", cartList);

// In another Servlet or JSP page
String user = (String) session.getAttribute("username"); // Retrieving the object
ArrayList<String> cart = (ArrayList<String>) session.getAttribute("cartItems");
