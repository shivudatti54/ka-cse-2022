java
class SharedResource {
private int data;
private boolean available = false;

    public synchronized void produce(int value) throws InterruptedException {
        while (available) {
            wait(); // Wait if data hasn't been consumed yet
        }
        data = value;
        available = true;
        System.out.println("Produced: " + data);
        notify(); // Notify the waiting consumer thread
    }

    public synchronized void consume() throws InterruptedException {
        while (!available) {
            wait(); // Wait if no data is available to consume
        }
        System.out.println("Consumed: " + data);
        available = false;
        notify(); // Notify the waiting producer thread
    }

}
