# **Multiple Threads, Using isAlive() and join(), Thread Priorities, Synchronization, Interthread Communication, Suspending, Resuming, and Stopping Thread**

## **Table of Contents**

- [Multiple Threads](#multiple-threads)
- [Using isAlive() and join()](#using-isalive-and-join)
- [Thread Priorities](#thread-priorities)
- [Synchronization](#synchronization)
- [Interthread Communication](#interthread-communication)
- [Suspending, Resuming, and Stopping Thread](#suspensing-resuming-and-stopping-thread)

## **Multiple Threads**

A thread is a separate flow of execution in a program. Multiple threads can run concurrently, improving the responsiveness and efficiency of a program.

**Key Concepts:**

- **Thread**: A separate flow of execution in a program.
- **Multithreading**: The use of multiple threads in a program.
- **Concurrency**: The ability of a program to execute multiple threads simultaneously.

**Example:**

```java
public class MultipleThreads {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread 1 started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Thread 1 finished");
            }
        });

        Thread thread2 = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread 2 started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Thread 2 finished");
            }
        });

        thread1.start();
        thread2.start();
    }
}
```

In this example, two threads (`thread1` and `thread2`) are created and started. Each thread runs concurrently, printing messages to the console.

## **Using isAlive() and join()**

The `isAlive()` method checks whether a thread is alive or not. The `join()` method waits for a thread to terminate.

**Key Concepts:**

- **isAlive()**: Checks whether a thread is alive or not.
- **join()**: Waits for a thread to terminate.

**Example:**

```java
public class UsingIsAliveAndJoin {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Thread finished");
            }
        });

        System.out.println("Initial state: " + thread.isAlive());

        thread.start();

        try {
            thread.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Final state: " + thread.isAlive());
    }
}
```

In this example, a thread is created and started. The main thread then waits for the created thread to terminate using the `join()` method. The `isAlive()` method is used to check the state of the thread before and after joining.

## **Thread Priorities**

Threads have different priorities. The main thread always has the highest priority.

**Key Concepts:**

- **Priority**: The priority of a thread.
- **Main thread**: The main thread always has the highest priority.

**Example:**

```java
public class ThreadPriorities {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread 1 started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Thread 1 finished");
            }
        });

        Thread thread2 = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread 2 started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Thread 2 finished");
            }
        });

        thread1.setPriority(Thread.MAX_PRIORITY);
        thread2.setPriority(Thread.MIN_PRIORITY);

        thread1.start();
        thread2.start();
    }
}
```

In this example, two threads are created with different priorities. The main priority is set to `Thread.MAX_PRIORITY` for `thread1` and `Thread.MIN_PRIORITY` for `thread2`.

## **Synchronization**

Synchronization is used to ensure that multiple threads access shared resources safely.

**Key Concepts:**

- **Synchronization**: Ensures that multiple threads access shared resources safely.
- **Lock**: A lock is used to synchronize access to shared resources.

**Example:**

```java
public class Synchronization {
    public static void main(String[] args) {
        int counter = 0;

        Thread thread1 = new Thread(new Runnable() {
            public void run() {
                for (int i = 0; i < 100000; i++) {
                    counter++;
                }
            }
        });

        Thread thread2 = new Thread(new Runnable() {
            public void run() {
                for (int i = 0; i < 100000; i++) {
                    counter++;
                }
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Final value of counter: " + counter);
    }
}
```

In this example, two threads are created to increment a shared counter variable. Without synchronization, the final value of the counter would be 0. However, with synchronization, the final value of the counter is 200000.

## **Interthread Communication**

Interthread communication is used to exchange data between threads.

**Key Concepts:**

- **Blocking queue**: A blocking queue is used to exchange data between threads.
- **Semaphore**: A semaphore is used to control access to shared resources.

**Example:**

```java
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class InterthreadCommunication {
    public static void main(String[] args) {
        BlockingQueue<String> queue = new LinkedList<>();

        ExecutorService executor = Executors.newFixedThreadPool(5);

        for (int i = 0; i < 10; i++) {
            executor.submit(new Producer(queue));
        }

        for (int i = 0; i < 10; i++) {
            executor.submit(new Consumer(queue));
        }

        executor.shutdown();

        try {
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Queue size: " + queue.size());
    }
}

class Producer implements Runnable {
    private BlockingQueue<String> queue;

    public Producer(BlockingQueue<String> queue) {
        this.queue = queue;
    }

    public void run() {
        for (int i = 0; i < 10; i++) {
            queue.add(String.valueOf(i));
        }
    }
}

class Consumer implements Runnable {
    private BlockingQueue<String> queue;

    public Consumer(BlockingQueue<String> queue) {
        this.queue = queue;
    }

    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println(queue.take());
        }
    }
}
```

In this example, two types of threads are created: producers and consumers. Producers add data to a shared blocking queue, while consumers remove data from the queue.

## **Suspending, Resuming, and Stopping Thread**

Threads can be suspended, resumed, or stopped using various methods.

**Key Concepts:**

- **suspend()**: Suspends a thread.
- **resume()**: Resumes a suspended thread.
- **stop()**: Stops a thread.

**Example:**

```java
public class SuspendingResumingStoppingThread {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread started");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Thread finished");
            }
        });

        thread.start();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Suspending thread");

        thread.suspend();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Resuming thread");

        thread.resume();

        try {
            thread.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Stopping thread");

        thread.stop();
    }
}
```

In this example, a thread is created and started. The main thread then suspends, resumes, and stops the created thread using various methods.
