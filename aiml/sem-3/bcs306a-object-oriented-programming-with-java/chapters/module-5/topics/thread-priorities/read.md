java
class CounterThread extends Thread {
    private String name;

    public CounterThread(String name) {
        this.name = name;
    }

    public void run() {
        int count = 0;
        // Perform a long, CPU-intensive task
        for (int i = 0; i < 1_000_000_000; i++) {
            count++;
            // Yield to let the scheduler decide who runs next
            Thread.yield();
        }
        System.out.println(name + " with priority " + this.getPriority() + " finished. Count: " + count);
    }
}

public class ThreadPriorityDemo {
    public static void main(String[] args) {
        // Create two threads
        CounterThread lowPriorityThread = new CounterThread("LowPriorityThread");
        CounterThread highPriorityThread = new CounterThread("HighPriorityThread");

        // Set their priorities
        lowPriorityThread.setPriority(Thread.MIN_PRIORITY); // 1
        highPriorityThread.setPriority(Thread.MAX_PRIORITY); // 10

        // Start the threads
        System.out.println("Starting threads...");
        lowPriorityThread.start();
        highPriorityThread.start();
    }
}