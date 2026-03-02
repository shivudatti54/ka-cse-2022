java
class ChildThread extends Thread {
    public void run() {
        for (int i = 0; i < 3; i++) {
            System.out.println("Child Thread: " + i);
            try { Thread.sleep(500); } catch (InterruptedException e) {}
        }
    }
}

public class IsAliveDemo {
    public static void main(String[] args) {
        ChildThread t = new ChildThread();
        System.out.println("Before start(): isAlive = " + t.isAlive()); // false

        t.start();
        System.out.println("After start(): isAlive = " + t.isAlive()); // true

        // Let main thread wait for child to finish
        try { t.join(); } catch (InterruptedException e) {}

        System.out.println("After child finished: isAlive = " + t.isAlive()); // false
    }
}