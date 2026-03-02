java
// 1. Creating the custom exception class (Checked)
class InvalidMarkException extends Exception {
    // 2. Provide constructors
    public InvalidMarkException() {
        super("Invalid mark provided!"); // Calls parent constructor
    }

    public InvalidMarkException(String message) {
        super(message); // Calls parent constructor with custom message
    }
}

// A class that uses the custom exception
public class MarkValidator {
    public void validateMark(int mark) throws InvalidMarkException {
        if (mark < 0 || mark > 100) {
            // 3. Throw the custom exception
            throw new InvalidMarkException("Mark must be between 0 and 100. Received: " + mark);
        }
        System.out.println("Mark is valid: " + mark);
    }

    public static void main(String[] args) {
        MarkValidator validator = new MarkValidator();
        try {
            validator.validateMark(105); // This will trigger the exception
        } catch (InvalidMarkException e) {
            System.err.println("Caught Exception: " + e.getMessage());
        }
    }
}