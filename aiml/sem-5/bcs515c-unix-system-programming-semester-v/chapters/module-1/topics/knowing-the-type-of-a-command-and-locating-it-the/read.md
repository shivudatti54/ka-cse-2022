# Knowing Command Types, Locating Commands, and Root Login in UNIX

## Introduction

In UNIX system programming, effectively interacting with the shell is a foundational skill. Two critical aspects of this interaction are understanding the different types of commands available and knowing precisely how to locate the program file the shell executes. Furthermore, the `root` user possesses unique privileges essential for system administration, making it a pivotal concept for any engineer managing a UNIX system.

## Core Concepts

### 1. Types of UNIX Commands

When you type a command like `ls` or `gcc`, the shell interprets it. Commands can be categorized as follows:

*   **Built-in (Internal) Commands:** These commands are part of the shell itself (e.g., `bash` or `csh`). They are executed directly by the shell without spawning a new process. This makes them very fast. Examples include `cd`, `echo`, `pwd`, `alias`, and `export`.
    *   **Example:** `cd /home/user` changes the working directory using the shell's internal logic.

*   **External Commands:** These are separate, executable program files located somewhere in the filesystem. When you run an external command, the shell searches for it and then executes it in a new sub-process. The vast majority of commands (like `ls`, `cp`, `vi`, `gcc`) are external.
    *   **Example:** Running `ls` causes the shell to find and execute the `/bin/ls` program.

### 2. Locating Commands: The `which` and `type` Utilities

Since external commands are just files, the shell needs to know where to find them. It looks through a list of directories stored in the `PATH` environment variable.

*   **`which` command:** The `which` utility is straightforward. It takes a command name as an argument and returns the full path to the executable that would be run if that command were typed.
    *   **Example:**