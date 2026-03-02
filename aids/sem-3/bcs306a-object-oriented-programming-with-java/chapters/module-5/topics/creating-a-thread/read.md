java
class MyThread extends Thread {
    // Override the run() method
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread is running: " + i);
            try {
                Thread.sleep(500); // Pauses the thread for 500 ms
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class ThreadExample {
    public static void main(String[] args) {
        MyThread thread = new MyThread(); // Create a Thread object
        thread.start(); // Start the thread, which calls run()

        // The main thread continues its own execution
        for (int i = 0; i < 5; i++) {
            System.out.println("Main thread: " + i);
        }
    }
}