java
public class IntegerTypesDemo {
    public static void main(String[] args) {
        byte numberOfStudents = 120;        // OK, within byte range
        // byte overflow = 130;             // Error! 130 > 127 (compile-time error)

        short temperature = -200;           // OK, within short range
        int populationOfIndia = 1_408_000_000; // Using underscore for readability
        long globalPopulation = 8_100_000_000L; // Note the 'L' suffix for long

        System.out.println("Byte value: " + numberOfStudents);
        System.out.println("Formatted int: " + populationOfIndia);
        System.out.println("Long value: " + globalPopulation);

        // Arithmetic operations
        int a = 10;
        int b = 3;
        int result = a / b; // Integer division: result is 3, not 3.333...
        System.out.println("Result of 10/3: " + result);
    }
}