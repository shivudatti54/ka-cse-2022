### Purpose  
Understanding **User‑Defined Exceptions** is essential for building robust, maintainable C++ applications. By creating custom exception types, programmers can communicate domain‑specific errors clearly, separate error‑handling logic from business logic, and provide richer debugging information—skills that are vital in real‑world software development.

### Learning Objectives  
- **Explain** the rationale and benefits of using user‑defined exceptions in C++ programs.  
- **Design** custom exception classes that inherit from `std::exception` (or other standard base classes).  
- **Throw** and **catch** user‑defined exceptions to handle application‑specific error conditions.  
- **Demonstrate** proper use of exception specifications, virtual inheritance, and `what()` override.  
- **Apply** exception‑safety principles (e.g., RAII, no‑throw guarantees) when implementing custom exceptions.  
- **Analyze** the differences between built‑in and user‑defined exceptions and choose appropriate strategies.  
- **Integrate** custom exceptions into a sample program to improve error reporting and traceability.  
- **Evaluate** the impact of user‑defined exceptions on code readability, maintainability, and performance.