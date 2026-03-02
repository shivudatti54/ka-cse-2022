java
class OldSuspendResume extends Thread {
    public void run() {
        System.out.println("Thread is running...");
        try {
            Thread.sleep(1000); // Simulating work
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Thread completed.");
    }

    public static void main(String[] args) {
        OldSuspendResume t1 = new OldSuspendResume();
        t1.start();

        try {
            Thread.sleep(500); // Let the thread run for a bit
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        t1.suspend(); // DEPRECATED & UNSAFE: Suspends the thread

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        t1.resume(); // DEPRECATED & UNSAFE: Resumes the thread
    }
}