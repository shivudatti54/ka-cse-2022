# Coprocesses in Unix/Linux

## Introduction

Coprocesses represent an advanced mechanism for inter-process communication (IPC) in Unix/Linux shell programming, enabling bidirectional data exchange between a shell and background processes. Unlike conventional background jobs initiated with the `&` operator, coprocesses establish a full-duplex communication channel through dedicated file descriptors, facilitating real-time interactive data exchange between the parent shell and the child process.

The concept of coprocesses was originally introduced in the Korn Shell (ksh) and subsequently incorporated into Bash (version 4.0 and later). This feature demonstrates fundamental operating system concepts including pipe creation, file descriptor management, and process synchronization. In the context of computer science education, coprocesses serve as a practical illustration of IPC mechanisms that underpin client-server architectures, data processing pipelines, and automation frameworks.

## Theoretical Background

### Inter-Process Communication Fundamentals

Unix systems provide multiple IPC mechanisms including pipes, message queues, shared memory, and sockets. Coprocesses specifically utilize **unnamed pipes** (created via the `pipe()` system call) to establish communication channels. A pipe is a unidirectional byte stream; for bidirectional communication, two pipes are required—one for each direction.

The file descriptor model forms the foundation of coprocess communication. Each process maintains a file descriptor table indexed by non-negative integers. When a coprocess is created, the shell:

1. Creates a pipe for parent-to-child communication (writing to child)
2. Creates a pipe for child-to-parent communication (reading from child)
3. Duplicates appropriate pipe ends onto stdin (fd 0) and stdout (fd 1) of the child process
4. Stores the remaining pipe ends in an array variable for shell access

### Formal Definition

A coprocess can be formally defined as a tuple `(PID, FD_read, FD_write)` where:

- `PID`: Process identifier of the background command
- `FD_read`: File descriptor for reading the coprocess's standard output
- `FD_write`: File descriptor for writing to the coprocess's standard input

## Syntax and Implementation

### Basic Syntax

```bash
coproc NAME { commands; }
coproc NAME ( commands )
```

If no name is specified, Bash defaults to `COPROC`. The shell creates an array variable where:

- `${NAME[0]}`: File descriptor for reading (connected to command's stdout)
- `${NAME[1]}`: File descriptor for writing (connected to command's stdin)
- `${NAME_PID}`: Process ID of the coprocess

### File Descriptor Mapping

| Array Element | File Descriptor | Purpose                          |
| ------------- | --------------- | -------------------------------- |
| `${NAME[0]}`  | Read end        | Parent reads command's stdout    |
| `${NAME[1]}`  | Write end       | Parent writes to command's stdin |
| `${NAME_PID}` | N/A             | Process identifier               |

### Syntax Variations

```bash
# Basic named coprocess
coproc BC { bc -l; }

# Command substitution syntax
coproc AWK (awk '{print toupper($0)}')

# With stderr redirection
coproc FETCH { wget -q -O - http://example.com 2>&1; }

# Multiple commands in pipeline
coproc PROCESSOR { while read line; do echo "Processed: $line"; done; }
```

## Working Mechanism

### Internal Implementation

When executing `coproc NAME { cmd; }`, Bash performs the following operations:

1. **Fork**: Creates a child process via `fork()`
2. **Pipe Creation**: Calls `pipe()` twice to create two unnamed pipes
3. **Redirection**: Redirects stdin and stdout of the child process to respective pipe ends
4. **Execution**: Executes the command using `execvp()` or similar
5. **Descriptor Storage**: Stores accessible pipe ends in the `NAME` array
6. **Background Execution**: The parent continues without waiting for child completion

### Process Synchronization

The parent and coprocess operate concurrently. The parent must manage:

- **Read timing**: Using `read -t timeout` to prevent blocking
- **Write ordering**: Ensuring data is written before attempting to read
- **EOF handling**: Closing write end to signal end-of-input to the coprocess
- **Process termination**: Using `wait` to reap the child process

## Examples

### Example 1: Mathematical Calculator

```bash
#!/bin/bash

coproc BC { bc -l; }

echo "scale=4; 10 / 3" >&${BC[1]}
echo "2^10" >&${BC[1]}
echo "sqrt(100)" >&${BC[1]}
echo "quit" >&${BC[1]}

while read -t 1 line <&${BC[0]}; do
 echo "Result: $line"
done

wait $BC_PID
```

**Output:**

```
Result: 3.3333
Result: 1024
Result: 10.0000
```

### Example 2: Data Transformation Pipeline

```bash
#!/bin/bash

coproc AWK { awk '{print toupper($0)}'; }

echo "hello world" >&${AWK[1]}
echo "unix operating system" >&${AWK[1]}

exec ${AWK[1]}>&-

while read -t 2 line <&${AWK[0]}; do
 echo "Processed: $line"
done
```

**Output:**

```
Processed: HELLO WORLD
Processed: UNIX OPERATING SYSTEM
```

### Example 3: Interactive Server Process

```bash
#!/bin/bash

coproc SERVER {
 while read -r cmd; do
 case "$cmd" in
 "hello") echo "Hello, World!" ;;
 "date") date ;;
 "quit") break ;;
 *) echo "Unknown: $cmd" ;;
 esac
 done
}

echo "hello" >&${SERVER[1]}
echo "date" >&${SERVER[1]}
echo "quit" >&${SERVER[1]}

while read -t 1 line <&${SERVER[0]}; do
 echo "Server: $line"
done
```

### Example 4: Combined stdout/stderr Handling

```bash
#!/bin/bash

coproc BC { bc -l 2>&1; }

echo "scale=2; 5 + 3" >&${BC[1]}
echo "scale=2; 10 / 0" >&${BC[1]}

exec 3<&${BC[0]}

while read -u 3 line; do
 echo "BC: $line"
done

wait $BC_PID
```

## Best Practices and Error Handling

1. **Descriptor Management**: Always close `${NAME[1]}` after writing to signal EOF to the coprocess
2. **Process Reaping**: Use `wait $NAME_PID` to prevent zombie processes
3. **Timeout Handling**: Employ `read -t seconds` to avoid indefinite blocking
4. **Error Checking**: Verify `${NAME_PID}` is set after coprocess creation
5. **Default Naming**: Remember that unnamed coprocesses use `COPROC`
6. **Bidirectional Flow**: Unlike `&`, coprocesses enable stdin/stdout communication simultaneously
