java
class PriorityDemo extends Thread {
    public void run() {
        // Print the priority of the current thread
        System.out.println(Thread.currentThread().getName() + " Priority: " + Thread.currentThread().getPriority());
        
        // A simple task: print numbers
        for (int i = 0; i < 3; i++) {
            System.out.println(Thread.currentThread().getName() + " Count: " + i);
            try {
                Thread.sleep(500); // Simulate some work with sleep
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        // Create two thread objects
        PriorityDemo t1 = new PriorityDemo();
        PriorityDemo t2 = new PriorityDemo();

        // Set their names for identification
        t1.setName("High Priority Thread");
        t2.setName("Low Priority Thread");

        // Set their priorities
        t1.setPriority(Thread.MAX_PRIORITY); // Priority 10
        t2.setPriority(Thread.MIN_PRIORITY);  // Priority 1

        // Start the threads
        t1.start();
        t2.start();
    }
}