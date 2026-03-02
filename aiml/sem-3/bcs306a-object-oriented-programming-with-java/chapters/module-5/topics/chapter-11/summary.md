# Chapter 11 Revision Notes

### Introduction

- Overview of Java Thread Model
- Importance of Multithreading in Java

### Key Concepts

- **Thread Class Hierarchy**
  - `Thread` (base class)
  - `Runnable` (interface)
  - `ThreadGroup` (container for threads)
- **Thread States**
  - New
  - Runnable
  - Running
  - Waiting
  - Blocked
  - Dead
- **Thread Life Cycle**
  - Creation
  - Synchronization
  - Termination

### Creating Threads

- **Extending the Thread Class**
  - Create a subclass of `Thread`
  - Override the `run()` method
- **Implementing the Runnable Interface**
  - Implement the `run()` method
  - Create a `Thread` object, passing an instance of the implementing class

### Synchronization and Communication

- **Synchronization**
  - `synchronized` keyword
  - `synchronized` blocks
  - `lock` objects
- **Communication between Threads**
  - `wait()`, `notify()`, and `notifyAll()` methods
  - `Lock` objects

### Important Formulas and Definitions

- **Thread Priority**
  - `ThreadPriority` enum
  - Formula: `ThreadPriority` = priority \* 10
- **Thread Synchronization**
  - Definition: ensuring that only one thread can access shared resources at a time

### Theorems and Principles

- **Multithreading Theorem**: A program can execute multiple threads concurrently.
- **Lamport's Bakery Algorithm**: A method for synchronizing threads using wait-notify pairs.

This summary should provide a concise review of the key concepts and important points in Chapter 11 of Object-Oriented Programming with Java.
