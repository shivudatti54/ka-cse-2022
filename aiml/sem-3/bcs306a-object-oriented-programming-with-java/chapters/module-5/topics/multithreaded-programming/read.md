java
class MyThread extends Thread {
    @Override
    public void run() {
        // Code that will be executed by this thread
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread is running: " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t1 = new MyThread(); // Thread is in NEW state
        t1.start(); // Moves thread to RUNNABLE state
        // The main thread continues its own execution
    }
}