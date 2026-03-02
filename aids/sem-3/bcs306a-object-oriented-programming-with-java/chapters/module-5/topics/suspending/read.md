java
class MyThread extends Thread {
    public void run() {
        for(int i=0; i<5; i++) {
            System.out.println(Thread.currentThread().getName() + ": " + i);
            try {
                Thread.sleep(500); // Sleep for 500ms
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class SuspendResumeExample {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start();

        try {
            Thread.sleep(1500); // Let main thread sleep
            t1.suspend(); // Suspend t1 after ~1.5 seconds
            System.out.println("Thread Suspended");

            Thread.sleep(1500); // Main thread sleeps again
            t1.resume(); // Resume t1 after another ~1.5 seconds
            System.out.println("Thread Resumed");

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}