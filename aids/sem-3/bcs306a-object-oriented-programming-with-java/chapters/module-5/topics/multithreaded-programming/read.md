java
class MyThread extends Thread {
    @Override
    public void run() {
        // Code that will be executed in this thread
        System.out.println("Thread is running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start(); // Starts the thread, which calls run()
    }
}