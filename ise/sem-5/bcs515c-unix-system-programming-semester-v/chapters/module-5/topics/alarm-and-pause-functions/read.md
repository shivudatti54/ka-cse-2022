# Module 5: Alarm and Pause Functions in UNIX System Programming

## 1. Introduction

In process control and signal handling, managing time and synchronizing process execution are crucial tasks. The `alarm()` and `pause()` system calls are two fundamental functions used for this purpose. They allow a process to schedule a signal for itself after a specified time and then wait for any signal to arrive, providing a simple mechanism for timed waiting and timeout handling.

---

## 2. Core Concepts & Explanation

### The `alarm()` Function

The `alarm()` function is used to set a timer that will send a `SIGALRM` signal to the calling process after a specified number of real (wall-clock) seconds.

**Syntax:**
