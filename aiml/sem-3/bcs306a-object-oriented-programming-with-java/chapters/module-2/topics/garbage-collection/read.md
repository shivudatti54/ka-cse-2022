java
public class GCDemo {
    public static void main(String[] args) {
        // Object 'obj1' is created and is reachable via this reference
        GCDemo obj1 = new GCDemo();

        // A new object is created; 'obj1' now references this new object.
        // The first object becomes unreachable and eligible for GC.
        obj1 = new GCDemo();

        // Method call creates a local reference 'obj2'
        createObject();
        // After the method returns, 'obj2' goes out of scope.
        // The object created inside the method becomes unreachable.
    }

    static void createObject() {
        GCDemo obj2 = new GCDemo(); // Object is reachable inside this method
    } // 'obj2' goes out of scope here. The object becomes unreachable.
}