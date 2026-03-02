java
public class MainThreadDemo {
    public static void main(String[] args) {
        // Get a reference to the currently executing thread (the Main Thread)
        Thread t = Thread.currentThread();

        // Display thread information
        System.out.println("Current Thread: " + t);

        // Change the name of the main thread
        t.setName("MyMainThread");
        System.out.println("After name change: " + t);

        // Demonstrate thread execution
        for (int i = 5; i > 0; i--) {
            System.out.println(i);
            try {
                Thread.sleep(1000); // Pause execution for 1 second
            } catch (InterruptedException e) {
                System.out.println("Main thread interrupted");
            }
        }
        System.out.println("Main thread exiting.");
    }
}