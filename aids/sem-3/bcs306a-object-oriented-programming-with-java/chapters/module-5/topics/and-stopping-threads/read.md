java
class MyThread extends Thread {
    @Override
    public void run() {
        // Code to be executed in the new thread
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread running: " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // Starts the new thread; calls run()
    }
}