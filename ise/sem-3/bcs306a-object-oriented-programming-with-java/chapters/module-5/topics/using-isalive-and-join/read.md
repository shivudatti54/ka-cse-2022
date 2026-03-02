java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running...");
        try {
            Thread.sleep(2000); // Simulate some work
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Thread finishing.");
    }
}

public class IsAliveDemo {
    public static void main(String[] args) {
        MyThread th = new MyThread();
        
        System.out.println("Before start(): " + th.isAlive()); // false
        
        th.start();
        System.out.println("After start(): " + th.isAlive()); // true
        
        // Wait a bit for the thread to finish
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        System.out.println("After thread finished: " + th.isAlive()); // false
    }
}