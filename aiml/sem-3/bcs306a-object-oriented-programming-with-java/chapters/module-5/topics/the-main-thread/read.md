java
public class MainThreadDemo {
    public static void main(String[] args) {
        // Get a reference to the current thread, which is the main thread.
        Thread mainThread = Thread.currentThread();

        // Display thread information
        System.out.println("Current Thread: " + mainThread);
        System.out.println("Name: " + mainThread.getName());
        System.out.println("Priority: " + mainThread.getPriority());
        System.out.println("Is Alive? " + mainThread.isAlive());

        // Change the name of the main thread
        mainThread.setName("PrimaryThread");
        System.out.println("New Name: " + mainThread.getName());
    }
}