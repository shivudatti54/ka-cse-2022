# Knowing the Type of a Command and Locating It: The Root Login

## Introduction

In the UNIX/Linux ecosystem, understanding the nature of commands and their location on the filesystem is a fundamental system administration and programming skill. As a user, especially the all-powerful `root`, you interact with the system by executing commands. These commands are not magic; they are files stored in specific directories. This module covers how to determine what kind of file a command is and how to find its exact location, with a specific focus on the privileged context of the `root` user.

## Core Concepts

### 1. Types of Commands (Programs)

In UNIX, a "command" is typically one of four types of files:

- **Built-in Commands (Shell Builtins):** These are commands that are built directly into the shell program (e.g., `bash`, `csh`). They don't exist as separate files on the disk. Examples include `cd`, `echo`, `alias`, and `exit`. They are executed quickly because no new process needs to be created.
- **External Commands (Binary Executables):** These are compiled programs stored as executable files on the filesystem. They are usually located in directories like `/bin`, `/usr/bin`, `/sbin`, or `/usr/sbin`. Examples include `ls`, `cp`, `gcc`, and `vi`. When you run them, the shell forks a new process to execute them.
- **Shell Scripts:** These are text files containing a sequence of shell commands. They begin with a shebang (`#!`) line specifying the interpreter to use (e.g., `#!/bin/bash`). They require both read and execute permissions.
- **Aliases:** These are user-defined shortcuts for commands or sequences of commands, created using the `alias` shell built-in. They are not files but reside in the shell's memory.

### 2. Locating a Command: The `which` and `type` Commands

To identify a command's type and location, you use specific tools:

- **`type` command:** This is a shell builtin that is most commonly used and highly reliable. It tells you exactly what the shell will execute when you run a given command name.
