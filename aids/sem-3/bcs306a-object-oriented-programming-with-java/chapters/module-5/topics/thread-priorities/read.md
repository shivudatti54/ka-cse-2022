java
class HighPriorityThread extends Thread {
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("High Priority Thread: " + i);
        }
    }
}

class LowPriorityThread extends Thread {
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Low Priority Thread: " + i);
        }
    }
}

public class ThreadPriorityDemo {
    public static void main(String[] args) {
        HighPriorityThread t1 = new HighPriorityThread();
        LowPriorityThread t2 = new LowPriorityThread();

        // Set priorities
        t1.setPriority(Thread.MAX_PRIORITY); // Value: 10
        t2.setPriority(Thread.MIN_PRIORITY); // Value: 1

        // Start the threads
        t2.start(); // Start lower priority first
        t1.start(); // Then start higher priority
    }
}