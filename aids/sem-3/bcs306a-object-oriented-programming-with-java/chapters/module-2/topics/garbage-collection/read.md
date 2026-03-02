java
public class GarbageCollectionDemo {
    public static void main(String[] args) {
        // Object 1 is created and referenced by 'obj1'
        GarbageCollectionDemo obj1 = new GarbageCollectionDemo();

        // Object 2 is created and referenced by 'obj2'
        GarbageCollectionDemo obj2 = new GarbageCollectionDemo();

        // obj1 is now reassigned to reference Object 2.
        // The original Object 1 is now unreachable and eligible for GC.
        obj1 = obj2;

        // We nullify 'obj2'. Now both obj1 and obj2 point to Object 2.
        // But Object 2 is still reachable through 'obj1'.
        obj2 = null;

        // Now we nullify 'obj1'. Object 2 is now unreachable.
        // Both Object 1 and Object 2 are eligible for garbage collection.
        obj1 = null;

        // Suggesting JVM to run Garbage Collector (it may or may not run)
        System.gc();
    }

    // This finalize method is overridden to show when an object is collected.
    // This is for demonstration only; avoid using finalize() in real projects.
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Garbage collector collected object: " + this);
    }
}