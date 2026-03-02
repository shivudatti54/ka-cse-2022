java
// 1. Create a class extending Exception (checked)
class InvalidAgeException extends Exception {
    
    // 2. Provide Constructors
    public InvalidAgeException() {
        super("Age is invalid"); // Call parent constructor
    }
    
    public InvalidAgeException(String message) {
        super(message); // Call parent constructor with custom message
    }
    
    // Optional: Constructor for chaining
    public InvalidAgeException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Usage in a method
public void setAge(int age) throws InvalidAgeException {
    if (age < 0 || age > 120) {
        // 3. Throw the custom exception
        throw new InvalidAgeException("Age must be between 0 and 120. Provided: " + age);
    }
    this.age = age;
}