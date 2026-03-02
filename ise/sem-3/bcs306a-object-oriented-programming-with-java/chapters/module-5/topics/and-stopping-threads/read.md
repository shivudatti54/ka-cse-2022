java
class MyTask implements Runnable {
@Override
public void run() {
for (int i = 0; i < 5; i++) {
System.out.println(Thread.currentThread().getName() + ": " + i);
try {
Thread.sleep(500); // Simulate some work
} catch (InterruptedException e) {
e.printStackTrace();
}
}
}
}

public class ThreadDemo {
public static void main(String[] args) {
// Create a Runnable object
MyTask task = new MyTask();

        // Create a Thread object and pass the Runnable to it
        Thread workerThread = new Thread(task, "WorkerThread");

        // Start the thread - JVM calls run() in a new call stack
        workerThread.start(); // Correct way

        // This runs in the main thread
        for (int i = 0; i < 5; i++) {
            System.out.println(Thread.currentThread().getName() + ": " + i);
        }

        // workerThread.run(); // WRONG! This would run MyTask.run in the main thread.
    }

}
