java
try {
// Code that may throw an exception
int result = 10 / 0; // This will throw an ArithmeticException
}
catch (ArithmeticException e) {
// Handle the specific exception
System.out.println("Cannot divide by zero: " + e.getMessage());
}
catch (Exception e) {
// A generic catch block for any other Exception type
System.out.println("An error occurred: " + e.getMessage());
}
finally {
// This code always runs
System.out.println("This is the finally block. Cleanup here.");
}
