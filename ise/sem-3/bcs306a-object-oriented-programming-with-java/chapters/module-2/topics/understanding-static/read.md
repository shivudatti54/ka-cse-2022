java
class Example {
static int importantValue;

    // Static Block
    static {
        importantValue = initializeImportantValue(); // a complex calculation
        System.out.println("Static block executed. Class loaded.");
    }

    static int initializeImportantValue() {
        return 100; // Simulated complex calculation
    }

}
