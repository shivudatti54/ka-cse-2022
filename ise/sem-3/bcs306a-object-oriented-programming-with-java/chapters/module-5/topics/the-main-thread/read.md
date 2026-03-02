java
// File: MainThreadDemo.java
public class MainThreadDemo {
    public static void main(String[] args) {
        // Get a reference to the currently executing thread (the main thread)
        Thread t = Thread.currentThread();

        // Display the thread's default name
        System.out.println("Current thread: " + t.getName());

        // Change the name of the main thread
        t.setName("MyMainThread");
        System.out.println("After name change: " + t.getName());

        // Get the priority of the main thread (default is 5)
        System.out.println("Main thread priority: " + t.getPriority());

        // This will also print the thread's name, priority, and its thread group.
        System.out.println("Thread info: " + t);

        // Let's see the sequence of execution within the main thread
        for (int i = 5; i > 0; i--) {
            System.out.println(i);
            try {
                Thread.sleep(1000); // Pause the main thread for 1000 milliseconds (1 second)
            } catch (InterruptedException e) {
                System.out.println("Main thread interrupted");
            }
        }
        System.out.println("Exiting the main thread.");
    }
}