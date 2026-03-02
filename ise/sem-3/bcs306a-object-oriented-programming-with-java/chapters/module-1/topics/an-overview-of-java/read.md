# Module 1: An Overview of Java

## Introduction

Java is a high-level, robust, object-oriented programming language and platform developed by Sun Microsystems (now owned by Oracle) in 1995. For engineering students, Java is foundational because of its principle of **"Write Once, Run Anywhere" (WORA)**, made possible by the Java Virtual Machine (JVM). Its architecture-neutral nature, security features, and vast ecosystem of libraries make it one of the most widely used languages for building everything from enterprise-scale applications to Android apps.

---

## Core Concepts

### 1. Java Platforms: JDK, JRE, and JVM

Understanding the difference between these three is crucial:

*   **JVM (Java Virtual Machine):** An abstract machine that provides the runtime environment to execute Java bytecode. It is platform-dependent (you need a Windows JVM for Windows, a Linux JVM for Linux, etc.) and is responsible for making Java portable.
*   **JRE (Java Runtime Environment):** The on-disk system that exists on a user's computer. It contains the JVM, class libraries, and other files necessary to *run* Java programs. It does not contain development tools like a compiler or debugger.
*   **JDK (Java Development Kit):** The full-featured SDK for Java. It contains the JRE *plus* development tools such as the compiler (`javac`), debugger (`jdb`), and archiver (`jar`). **As a developer, you need the JDK.**

**Analogy:** If JVM is the engine of a car, JRE is the car itself, and JDK is the car manufacturing plant with all the tools.

### 2. The Java Compilation and Execution Process

Java's "Write Once, Run Anywhere" magic happens in two distinct steps:

1.  **Compilation:** The Java source code (`.java` file) is compiled by the `javac` compiler. This does not produce native machine code. Instead, it produces **bytecode** (an intermediate, platform-neutral code) stored in a `.class` file.
2.  **Execution:** The `.class` file is given to the JVM. The JVM, which is specific to the host operating system, reads the bytecode and interprets it into native machine instructions for execution. Modern JVMs use a **Just-In-Time (JIT)** compiler to compile frequently used bytecode into native code for significant performance improvements.