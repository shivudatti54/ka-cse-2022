java
// Class representing the task for a thread
class MyThread extends Thread {
private String threadName;

    MyThread(String name) {
        this.threadName = name;
    }

    // This is the entry point for the new thread
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(threadName + " is running... " + i);
            try {
                // Sleep for a short period to simulate work
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(threadName + " interrupted.");
            }
        }
        System.out.println(threadName + " exiting.");
    }

}

public class MultiThreadDemo {
public static void main(String[] args) {
// Create multiple thread objects
MyThread threadA = new MyThread("Thread-A");
MyThread threadB = new MyThread("Thread-B");
MyThread threadC = new MyThread("Thread-C");

        // Start the threads. Order of execution is NOT guaranteed.
        threadA.start();
        threadB.start();
        threadC.start();

        // The main thread continues its own execution
        System.out.println("Main thread exiting.");
    }

}
