java
class MyThread extends Thread {
    // Override the run method
    public void run() {
        for(int i = 0; i < 5; i++) {
            System.out.println("Thread is running: " + i);
            try {
                Thread.sleep(500); // Simulate some work
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class ThreadExample {
    public static void main(String[] args) {
        MyThread thread = new MyThread(); // Create thread object
        thread.start(); // Start the thread (invokes run())
        
        // Code in the main thread continues concurrently
        for(int i = 0; i < 5; i++) {
            System.out.println("Main thread: " + i);
        }
    }
}