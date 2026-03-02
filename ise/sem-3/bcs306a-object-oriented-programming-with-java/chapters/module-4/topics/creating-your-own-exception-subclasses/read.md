java
// This is a Checked Exception because it extends Exception
class InvalidAgeException extends Exception {

    // Constructor 1: Default
    public InvalidAgeException() {
        super("Invalid age provided."); // Passes a default message to the parent class
    }

    // Constructor 2: With a custom message
    public InvalidAgeException(String message) {
        super(message); // Passes the custom message to the parent class
    }

}

public class UserRegistration {
public void registerUser(int age) throws InvalidAgeException {
if (age < 18) {
// Throw our custom checked exception
throw new InvalidAgeException("Age must be 18 or older.");
}
// Proceed with registration
System.out.println("User registered successfully.");
}

    public static void main(String[] args) {
        UserRegistration reg = new UserRegistration();
        try {
            reg.registerUser(16); // This will throw the exception
        } catch (InvalidAgeException e) {
            System.err.println("Registration failed: " + e.getMessage());
        }
    }

}
