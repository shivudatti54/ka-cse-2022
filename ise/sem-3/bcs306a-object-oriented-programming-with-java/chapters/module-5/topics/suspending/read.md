java
class DeprecatedExample {
public static void main(String[] args) {
Thread worker = new Thread(() -> {
while (true) {
System.out.println("Working...");
try { Thread.sleep(1000); } catch (InterruptedException e) {}
}
});

        worker.start();
        try { Thread.sleep(5000); } catch (InterruptedException e) {}

        // DEPRECATED AND UNSAFE
        worker.suspend(); // Suspends the thread
        System.out.println("Thread suspended for 3 seconds.");
        try { Thread.sleep(3000); } catch (InterruptedException e) {}

        // DEPRECATED AND UNSAFE
        worker.resume(); // Resumes the thread
        System.out.println("Thread resumed.");
    }

}
