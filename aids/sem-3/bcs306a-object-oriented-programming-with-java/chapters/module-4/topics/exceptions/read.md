java
try {
    // Code that might throw an exception
    int result = 10 / 0; // This will throw an ArithmeticException
}
catch (ArithmeticException e) {
    // Handler for ArithmeticException
    System.out.println("Cannot divide by zero: " + e.getMessage());
}