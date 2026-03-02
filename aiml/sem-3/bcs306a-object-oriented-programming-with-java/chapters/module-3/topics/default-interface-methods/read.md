java
interface MyInterface {
    // Regular abstract method
    void existingMethod(String str);

    // New default method
    default void newDefaultMethod() {
        System.out.println("This is the default implementation.");
        // Can call other methods within the interface
        privateHelperMethod();
    }

    // Static methods are also allowed in interfaces (Java 8+)
    static void staticUtilityMethod() {
        System.out.println("This is a static utility method.");
    }

    // Private methods (Java 9+) to break down default method logic
    private void privateHelperMethod() {
        System.out.println("Helper logic called from default method.");
    }
}