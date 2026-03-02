# The `finally` Block in Java

## Introduction

In Java, exception handling is managed through `try`, `catch`, and `throw` keywords. However, there are scenarios where you need to execute a block of code regardless of whether an exception occurred or was handled. This is the primary purpose of the `finally` block. It is a fundamental construct for writing robust and clean Java code, ensuring that critical cleanup operations, such as closing files or releasing network resources, are never accidentally skipped.

## Core Concepts

The `finally` block is an optional part of a `try-catch` statement. The key characteristic of this block is that the Java Runtime Environment (JRE) **always** executes it, no matter what happens in the corresponding `try` or `catch` blocks.

The execution flow is as follows:

1.  The code inside the `try` block is executed.
2.  If an exception occurs, the JVM looks for a matching `catch` block.
3.  Whether a matching `catch` block is found _or not_, and whether the exception is handled _or not_, the `finally` block is **guaranteed** to run.
4.  The only exceptions to this guarantee are if the JVM exits abruptly (e.g., `System.exit(0)`) or if the executing thread is interrupted.

### Why is `finally` Important?

The main utility of `finally` is for **resource cleanup**. Consider a program that opens a file or a database connection inside a `try` block. If an exception is thrown while processing the data, the subsequent code to close the resource might be bypassed. This can lead to resource leaks. Placing the cleanup code (like `close()`) in a `finally` block ensures it runs, preventing such leaks.

## Syntax and Examples

The basic syntax for using a `finally` block is:
