# **Connecting Commands: Pipe**

## **Introduction**

In UNIX system programming, the pipe symbol (`|`) is a powerful tool for connecting commands. It allows you to redirect the output of one command as the input to another command. This enables you to perform complex operations in a single command, making your life easier and more efficient.

## **What is a Pipe?**

A pipe is a way to connect two or more commands together. It creates a pipeline of commands that execute one after the other, with the output of the previous command serving as the input for the next command.

## **How to Use a Pipe**

To use a pipe, you simply separate the commands with the pipe symbol (`|`). The output of the first command is piped to the input of the second command.

## **Example 1: Basic Pipe**

```bash
ls -l | grep keyword
```

In this example, the `ls -l` command lists the files in the current directory in a long format, and the `grep keyword` command searches for the keyword in the output.

**Key Concepts:**

- **Output Redirection**: The output of the first command is redirected to the input of the second command.
-     **Input Stream**: The output of the first command serves as the input stream for the second command.

## **Example 2: Pipe with Multiple Commands**

```bash
ls -l | grep keyword | less
```

In this example, the output of the `ls -l` command is piped to the `grep keyword` command to search for the keyword. The output of the `grep` command is then piped to the `less` command to display the results in a pager.

**Key Concepts:**

- **Multiple Commands**: You can pipe multiple commands together to perform complex operations.
- **Piping Multiple Outputs**: You can pipe the output of one command to the input of another command.

## **Example 3: Pipe with `sort` and `uniq`**

```bash
ls -l | grep keyword | sort | uniq
```

In this example, the output of the `grep keyword` command is piped to the `sort` command to sort the results. The output of the `sort` command is then piped to the `uniq` command to remove duplicate lines.

**Key Concepts:**

- **Sorting and Uniquing**: You can use the `sort` and `uniq` commands to sort and remove duplicate lines from the output.

## **Best Practices**

- **Use the pipe symbol (`|`) to connect commands**: This creates a pipeline of commands that execute one after the other.
- **Use output redirection to redirect output**: This allows you to redirect the output of one command to the input of another command.
- **Use input streams to pass data between commands**: This allows you to pass data between commands in a pipeline.

By mastering the pipe command, you can create complex pipelines to perform a wide range of operations. Remember to use output redirection and input streams to pass data between commands, and always use the pipe symbol (`|`) to connect commands.
