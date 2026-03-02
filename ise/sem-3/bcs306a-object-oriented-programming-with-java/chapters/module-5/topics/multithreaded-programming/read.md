java
class MyThread extends Thread {
public void run() {
System.out.println("Thread is running...");
}
}

// In main method
MyThread t1 = new MyThread();
t1.start(); // Starts the thread, which calls run()
