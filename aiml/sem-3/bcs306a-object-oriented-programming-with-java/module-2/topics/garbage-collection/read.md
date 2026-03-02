# Garbage Collection in Java


## Table of Contents

- [Garbage Collection in Java](#garbage-collection-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Object Lifecycle and Memory Allocation](#object-lifecycle-and-memory-allocation)
  - [How Garbage Collection Works](#how-garbage-collection-works)
  - [Types of Garbage Collectors](#types-of-garbage-collectors)
  - [The System.gc() and Runtime.gc() Methods](#the-systemgc-and-runtimegc-methods)
  - [Object Finalization](#object-finalization)
  - [Memory Leaks in Java](#memory-leaks-in-java)
  - [Tuning Garbage Collection](#tuning-garbage-collection)
- [Examples](#examples)
  - [Example 1: Understanding Object Eligibility for GC](#example-1-understanding-object-eligibility-for-gc)
  - [Example 2: Memory Leak in Collection](#example-2-memory-leak-in-collection)
  - [Example 3: Finalize Method Demonstration](#example-3-finalize-method-demonstration)
- [Exam Tips](#exam-tips)

## Introduction

Garbage Collection (GC) is one of the most significant features of Java that distinguishes it from traditional programming languages like C and C++. In languages like C, programmers are responsible for manually allocating and deallocating memory using functions like malloc() and free(). This manual memory management often leads to common errors such as memory leaks, dangling pointers, and double-free errors, which can cause system crashes and security vulnerabilities.

Java introduces an automatic garbage collection mechanism that automatically identifies and reclaims memory occupied by objects that are no longer in use. This automatic memory management is part of the Java Runtime Environment (JRE) and runs as a background daemon thread. The garbage collector effectively eliminates the burden of memory management from programmers, allowing them to focus on business logic rather than worrying about memory allocation and deallocation.

Understanding garbage collection is crucial for Java developers for several reasons. First, it helps in writing efficient code by understanding object lifecycle and memory usage patterns. Second, it enables developers to tune application performance by adjusting garbage collection parameters. Third, it helps in diagnosing and resolving memory-related issues like OutOfMemoryError. For university examinations, garbage collection is a fundamental concept that tests the student's understanding of Java's memory management model.

## Key Concepts

### Object Lifecycle and Memory Allocation

When a Java program creates an object using the new keyword, memory is allocated from the heap—a portion of JVM memory dedicated to storing objects. The heap is divided into different generations (Young Generation, Old Generation, and Permanent Generation in older JVMs, or Metaspace in newer versions). Each object goes through a lifecycle: creation, usage, and eventual destruction when no longer reachable.

An object becomes eligible for garbage collection when there are no more references to it. References can be cleared in several ways: explicitly setting the reference variable to null, reassigning the reference to a new object, or when the method that created the object completes execution (if it's a local variable). Once an object loses all references, it becomes unreachable and qualifies for garbage collection during the next GC cycle.

### How Garbage Collection Works

The garbage collection process works in several phases:

1. **Mark Phase**: The garbage collector traverses all object references starting from root objects (stack variables, static fields, JNI references) and marks all reachable objects as "alive".

2. **Sweep Phase**: The collector scans through the heap and identifies unmarked objects (unreachable objects) as garbage.

3. **Compact Phase (optional)**: For some collectors, memory compaction moves live objects together to eliminate memory fragmentation, making memory allocation faster.

The Java Virtual Machine (JVM) uses various garbage collection algorithms that work on the principle of generational garbage collection. The heap is divided based on object age:

- **Young Generation**: Where newly created objects are stored. Most objects are short-lived, so this region is frequently garbage collected (Minor GC).
- **Old Generation**: Where objects that survive multiple garbage collection cycles in the Young Generation are promoted. This region is garbage collected less frequently (Major GC or Full GC).

### Types of Garbage Collectors

Java provides several garbage collection algorithms, and the choice depends on application requirements:

1. **Serial GC**: Uses a single thread for garbage collection. Suitable for small applications with single-threaded environments. Enabled with -XX:+UseSerialGC.

2. **Parallel GC (Throughput GC)**: Uses multiple threads for garbage collection, focusing on maximizing throughput. Suitable for applications where throughput is more important than pause times. Enabled with -XX:+UseParallelGC.

3. **Concurrent Mark Sweep (CMS) GC**: Designed to minimize pause times by performing most garbage collection work concurrently with application threads. Suitable for responsive applications. Enabled with -XX:+UseConcMarkSweepGC. Note: Deprecated in Java 9.

4. **G1 (Garbage First) GC**: A server-style garbage collector designed for large heaps with variable size. It divides the heap into regions and collects garbage region by region. Default garbage collector since Java 9. Enabled with -XX:+UseG1GC.

5. **ZGC (Z Garbage Collector)**: A scalable low-latency garbage collector designed for large heaps (TB scale). Performs all expensive work concurrently. Enabled with -XX:+UseZGC.

6. **Shenandoah**: A low-pause-time garbage collector that works concurrently with the application. Enabled with -XX:+UseShenandoahGC.

### The System.gc() and Runtime.gc() Methods

Java provides methods to request garbage collection, though they do not guarantee immediate collection:

```java
// Two ways to request garbage collection
System.gc();
Runtime.getRuntime().gc();
```

These methods are equivalent and suggest to the JVM that garbage collection is desirable. The JVM is free to ignore this suggestion. Calling System.gc() is generally discouraged in production code because it forces a full garbage collection, which can cause performance issues. It should only be used for debugging or in specific testing scenarios.

### Object Finalization

Before an object is garbage collected, the garbage collector calls the finalize() method (if overridden) to perform cleanup operations. This is similar to destructors in C++ but with important differences:

```java
@Override
protected void finalize() throws Throwable {
 // Resource cleanup code
 System.out.println("Object being finalized");
 super.finalize();
}
```

Key points about finalize():

- Called exactly once per object (unless the object is resurrected by making it reachable again)
- Not guaranteed to be called in a timely manner
- Can cause performance issues
- Deprecated since Java 9 (JEP 421)
- Should not be used for resource cleanup; use try-with-resources instead

### Memory Leaks in Java

Although Java has automatic garbage collection, memory leaks can still occur when objects are no longer needed but remain referenced. Common causes include:

1. **Unintentional object retention**: Adding objects to collections (ArrayList, HashMap) and forgetting to remove them
2. **Static references**: Holding references in static collections
3. **Inner class references**: Non-static inner classes implicitly hold references to outer class instances
4. **JNI memory leaks**: Native code memory not properly released
5. **ThreadLocal variables**: Not removed after use

Memory leaks manifest as gradual increase in memory usage and eventual OutOfMemoryError.

### Tuning Garbage Collection

JVM provides numerous parameters to tune garbage collection:

- **Heap Size**: -Xms (initial heap size), -Xmx (maximum heap size)
- **Young Generation Size**: -Xmn (young generation size), -XX:NewRatio (ratio of young to old generation)
- **Thread Stack Size**: -Xss (thread stack size)
- **GC Type**: -XX:+UseG1GC, -XX:+UseSerialGC, etc.

Example: java -Xms256m -Xmx1024m -XX:+UseG1GC MyApplication

## Examples

### Example 1: Understanding Object Eligibility for GC

```java
public class GCExample {
 public static void main(String[] args) {
 // Object created and referenced by 'a'
 String a = new String("Hello");

 // Another reference to the same object
 String b = a;

 // Original reference 'a' is set to null
 // Object is still reachable through 'b'
 a = null;

 // Now no references point to the object
 // Object becomes eligible for GC
 b = null;

 // Request garbage collection
 System.gc();
 }
}
```

**Explanation**: The object created by `new String("Hello")` becomes eligible for garbage collection only when all references (a and b) are set to null. Simply setting `a = null` doesn't make the object eligible because `b` still references it.

### Example 2: Memory Leak in Collection

```java
import java.util.ArrayList;
import java.util.List;

public class MemoryLeakExample {
 private static List<String> cache = new ArrayList<>();

 public static void addToCache(String data) {
 // Problem: Never removes items, causing memory leak
 cache.add(data);
 }

 public static void main(String[] args) {
 for (int i = 0; i < 1000000; i++) {
 addToCache("Data " + i);
 }
 System.out.println("Cache size: " + cache.size());
 // OutOfMemoryError likely here
 }
}
```

**Solution**: Use WeakHashMap or periodically clear the cache:

```java
import java.util.WeakHashMap;

public class FixedExample {
 private static WeakHashMap<String, String> cache = new WeakHashMap<>();

 public static void addToCache(String data) {
 cache.put(data, data);
 }
 // Objects will be automatically removed when GC runs
}
```

### Example 3: Finalize Method Demonstration

```java
public class FinalizeDemo {
 private static FinalizeDemo object;

 @Override
 protected void finalize() throws Throwable {
 System.out.println("finalize() called - object being garbage collected");
 object = this; // Resurrecting the object
 }

 public static void main(String[] args) throws InterruptedException {
 object = new FinalizeDemo();
 System.out.println("Object created");

 // Make object eligible for GC
 object = null;

 // Request GC
 System.gc();

 // Give time for finalize to complete
 Thread.sleep(1000);

 if (object != null) {
 System.out.println("Object resurrected!");
 }
 }
}
```

**Output**:

```
Object created
finalize() called - object being garbage collected
Object resurrected!
```

This demonstrates that finalize() can resurrect an object, but it's unreliable and should be avoided.

## Exam Tips

1. **Remember the definition**: Garbage Collection is an automatic process in Java that identifies and reclaims memory occupied by unreachable objects.

2. **Know how objects become eligible for GC**: Objects become eligible when they have no live references—set to null, reassigned, or when local variables go out of scope.

3. **Understand generational collection**: Young Generation stores new objects, Old Generation stores long-lived objects. Most GC activity happens in Young Generation (Minor GC).

4. **Key garbage collectors**: Serial (single thread), Parallel (throughput), CMS (low pause), G1 (default since Java 9), ZGC (low latency).

5. **System.gc() is a request, not a command**: The JVM may ignore garbage collection requests. Don't rely on it for program correctness.

6. **Finalize is deprecated**: Remember that finalize() was deprecated in Java 9 due to performance and reliability issues. Use try-with-resources instead.

7. **Memory leaks still possible**: Even with GC, improper coding practices (unbounded collections, static references) can cause memory leaks.

8. **GC root references**: Stack variables, static fields, and JNI references are GC roots. Objects reachable from these roots are not garbage collected.

9. **Difference from C/C++**: In Java, you cannot explicitly free memory. The JVM handles all memory deallocation automatically.

10. **OutOfMemoryError**: This error occurs when the JVM cannot allocate memory for new objects, indicating either memory leak or insufficient heap size.
