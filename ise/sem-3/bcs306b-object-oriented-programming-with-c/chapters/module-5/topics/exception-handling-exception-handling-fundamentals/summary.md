# **Exception Handling: Revision Notes**

### Exception Handling Fundamentals

- **Definition:** Exception handling is a way to handle runtime errors in C++ programs.
- **Exception Object:** An object of the `std::exception` class that represents a runtime error.
- **Throw Statement:** Used to throw an exception (e.g., `throw std::runtime_error("Error message");`).
- **try-catch Block:** Used to catch exceptions (e.g., `try { code } catch (std::exception& e) { handle e; }`).

### Handling Derived-Class Exceptions

- **Exception Inheritance:** Derived classes can inherit exceptions from base classes.
- **Catch-All Clause:** `catch(...)`: Can catch all exceptions, including those derived from a base class.
- **Specific Catch Clause:** `catch (SpecificException& e)`: Can catch only specific exceptions.

### Exception Handling Options

- **try-catch Block:** Can be used to handle exceptions in a single block of code.
- **Multiple try-catch Blocks:** Can be used to handle exceptions in separate blocks of code.
- **except Clause:** Can be used to specify a block of code to execute when an exception is caught.
- **finally Clause:** Can be used to specify a block of code to execute regardless of whether an exception is thrown.

### Applying Exception Handling

- **Use try-catch Blocks:** To handle exceptions in specific blocks of code.
- **Use Specific Catch Clauses:** To catch specific exceptions instead of all exceptions.
- **Use Rethrow Statements:** To rethrow an exception to propagate it up the call stack.
- **Use Exception Safety:** To ensure that an exception does not leave the program in an inconsistent state.

### Important Formulas, Definitions, and Theorems

- **Exception Safety Theorem:** A program with exception safety guarantees that an exception cannot leave the program in an inconsistent state.
- **Exception Propagation:** The process of rethrowing an exception to propagate it up the call stack.
- **Exception Handling Mechanism:** The C++ exception handling mechanism provides a way to handle runtime errors in a program.
