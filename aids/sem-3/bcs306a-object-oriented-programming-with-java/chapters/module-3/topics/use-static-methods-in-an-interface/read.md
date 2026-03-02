java
interface MyInterface {
    // Traditional Abstract Method (implicitly public abstract)
    void doSomething();

    // Static Method with implementation
    static void staticUtilityMethod() {
        System.out.println("This is a static utility method.");
        // Additional implementation logic here
    }
}