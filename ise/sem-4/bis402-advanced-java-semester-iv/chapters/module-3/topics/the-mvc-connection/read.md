java
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
// 1. Get input from request
int studentId = Integer.parseInt(request.getParameter("id"));

        // 2. Interact with the Model
        StudentDAO dao = new StudentDAO();
        Student student = dao.getStudentById(studentId); // Model fetches data

        // 3. Pass data to the View
        request.setAttribute("student", student);

        // 4. Forward to the JSP View
        RequestDispatcher dispatcher = request.getRequestDispatcher("studentDetails.jsp");
        dispatcher.forward(request, response);
    }
