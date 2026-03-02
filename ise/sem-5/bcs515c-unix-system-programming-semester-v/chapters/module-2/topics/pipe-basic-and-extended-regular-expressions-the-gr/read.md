# Module 2: Pipes and Regular Expressions in UNIX

## Introduction

Effective UNIX system programming hinges on mastering two powerful concepts: connecting processes and manipulating text. This module covers the **pipe**, a fundamental mechanism for inter-process communication (IPC), and **regular expressions**, a indispensable tool for pattern matching, primarily used with the `grep` command. Together, they form the backbone of the UNIX philosophy of writing small, modular programs that work together.

---

## Core Concepts

### 1. Pipe (`|`)

A pipe is a form of IPC that allows the output of one command to be used as the input for another command. It creates a one-way communication channel between two processes, typically a parent and its child. The data flows left-to-right, from the first command (`stdout`) to the second command (`stdin`), without creating any intermediate temporary file.

**Syntax:**
