java
class MyThread extends Thread {
    // Override the run() method
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread is running: " + i);
            try {
                Thread.sleep(500); // Pauses the thread for 500ms
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        // Create an instance of the thread
        MyThread thread = new MyThread();
        
        // Start the thread (DO NOT call run() directly)
        thread.start(); // JVM calls the run() method on a new thread
        
        // Code in the main thread continues independently
        for (int i = 0; i < 5; i++) {
            System.out.println("Main thread: " + i);
        }
    }
}