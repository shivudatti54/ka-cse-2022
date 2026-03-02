# Learning Objectives

After studying this topic, you should students able to:

1. Define the main thread as the first thread that begins execution when a Java program starts, executing the `main()` method.
2. Explain the lifecycle of the main thread, including its automatic creation by the JVM, execution of the `main()` method, and termination when the `main()` method completes or an exception is thrown.
3. Implement code to control the main thread, including setting its priority using `setPriority()` and name using `setName()`.
4. Compare the main thread with child threads, highlighting the main thread's unique characteristics, such as being the first thread to execute and executing the `main()` method.
5. Evaluate the role of the main thread in creating and starting additional child threads using the `Thread` class or `Runnable` interface.
6. Design a Java program that utilizes the main thread to create and manage additional threads, applying the concepts learned in this topic.
7. Explain how to use `Thread` class methods, such as `currentThread()`, `getName()`, `getPriority()`, `sleep()`, and `getId()`, to manipulate the main thread.
8. Justify the importance of handling `InterruptedException` when using `sleep()`, as it is a checked exception, and demonstrate how to handle it in code.
