java
// Class that extends Thread class
class MyThread extends Thread {
    private String threadName;
    
    MyThread(String name) {
        this.threadName = name;
    }
    
    // The run() method contains the code to be executed by the thread
    @Override
    public void run() {
        for(int i = 0; i < 3; i++) {
            System.out.println(threadName + " is running... " + i);
            try {
                // Sleep for a random time to simulate work
                Thread.sleep(500); 
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
        System.out.println(threadName + " exiting.");
    }
}

public class MultiThreadDemo {
    public static void main(String[] args) {
        // Create multiple thread objects
        MyThread threadA = new MyThread("Thread A");
        MyThread threadB = new MyThread("Thread B");
        MyThread threadC = new MyThread("Thread C");
        
        // Start the threads. Order of start != order of execution.
        threadA.start();
        threadB.start();
        threadC.start();
        
        // The main thread continues its own execution
        System.out.println("Main thread exiting.");
    }
}