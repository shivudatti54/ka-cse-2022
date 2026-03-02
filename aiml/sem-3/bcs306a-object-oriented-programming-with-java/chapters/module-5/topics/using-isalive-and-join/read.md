java
class ChildThread extends Thread {
    public void run() {
        for (int i = 0; i < 3; i++) {
            System.out.println("Child Thread: " + i);
            try { Thread.sleep(500); } 
            catch (InterruptedException e) {}
        }
    }
}

public class IsAliveDemo {
    public static void main(String[] args) {
        ChildThread t = new ChildThread();
        System.out.println("Before start(): " + t.isAlive()); // false
        t.start();
        System.out.println("After start(): " + t.isAlive());  // true

        // Main thread continues its work
        for (int i = 0; i < 3; i++) {
            System.out.println("Main Thread: " + i);
            try { Thread.sleep(500); } 
            catch (InterruptedException e) {}
        }

        // Check status at the end
        System.out.println("At the end: " + t.isAlive()); // false
    }
}