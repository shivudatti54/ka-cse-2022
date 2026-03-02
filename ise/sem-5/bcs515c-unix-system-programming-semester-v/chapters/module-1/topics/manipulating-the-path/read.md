# Manipulating the `PATH` Environment Variable in UNIX

## Introduction

In UNIX and Linux systems, the `PATH` is a fundamental **environment variable** that dictates where the shell searches for executable programs or commands. For system programmers and users alike, understanding how to view, set, and manipulate the `PATH` is crucial for efficient workflow, script execution, and software development. It eliminates the need to specify the full absolute path to a common command like `ls` or `gcc` every time you want to run it.

## Core Concepts

### 1. What is the `PATH` Variable?

The `PATH` variable is a colon (`:`) separated list of directories. When you type a command like `gcc` and press enter, the shell sequentially searches each directory in this list, from left to right, for an executable file named `gcc`. The search stops at the first match, and that program is executed.

### 2. Why is it Important?

- **Convenience:** Allows you to run frequently used commands from any directory without typing their full path.
- **Script Execution:** Ensures scripts and programs you develop can be run from anywhere if placed in a directory on the `PATH`.
- **Software Management:** Helps manage multiple versions of software tools by controlling which version is found first.

### 3. Viewing the Current PATH

To see your current `PATH`, use the `echo` command.
