java
try {
    // Code that might throw an exception
    int result = 10 / 0; // This line will throw an ArithmeticException
}
catch (ArithmeticException e) {
    // Handler for ArithmeticException
    System.out.println("Cannot divide by zero! " + e.getMessage());
}
System.out.println("Program continues after the catch block...");