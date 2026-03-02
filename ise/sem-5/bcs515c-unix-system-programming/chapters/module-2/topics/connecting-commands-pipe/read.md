# **Connecting Commands: Pipe**

## **Introduction**

In UNIX, the pipe symbol (`|`) is used to connect the output of one command to the input of another command. This allows you to create complex pipelines of commands that can perform multiple tasks in a single step. In this topic, we will explore the concept of pipes and how to use them to connect commands.

## **What is a Pipe?**

A pipe is a redirection operator that connects the output of one command to the input of another command. The output of the first command is redirected to the input of the second command, allowing them to work together to achieve a common goal.

## **Basic Syntax**

The basic syntax of a pipe is as follows:

```bash
command1 | command2
```

Here, `command1` is the command that produces output, and `command2` is the command that processes that output.

## **How Pipes Work**

Here's a step-by-step explanation of how pipes work:

1. The output of `command1` is sent to the pipe.
2. The pipe reads the output of `command1` and passes it to `command2`.
3. `command2` processes the output and produces its own output.
4. The output of `command2` is sent to the standard output (usually the console).

## **Examples**

### Example 1: Simple Pipe

Suppose we have two commands: `cat` and `grep`. We can use a pipe to pipe the output of `cat` to `grep`:

```bash
$ cat file.txt | grep keyword
```

This command will print the lines that contain the word "keyword" from the file `file.txt`.

### Example 2: Pipe with Multiple Commands

We can use pipes to chain multiple commands together to achieve a complex task:

```bash
$ ls -l | grep keyword | more
```

This command will list the files and directories in the current directory in long format, then pipe the output to `grep` to find lines that contain the word "keyword", and finally pipe the output to `more` to print it on the screen.

## **Key Concepts**

- **Pipe symbol (`|`)**: Connects the output of one command to the input of another command.
- **Redirection operator**: Directs the output of one command to the input of another command.
- **Standard output (stdout)**: The default output of a command, usually sent to the console.
- **Standard input (stdin)**: The default input of a command, usually read from the console.

## **Practice Exercises**

1.  Practice piping commands to achieve the following tasks:
    - List the files and directories in the current directory and print only the files that are hidden.
    - Pipe the output of `ls -l` to `grep` to find lines that contain the word "keyword".
2.  Use pipes to chain multiple commands together to achieve a complex task.

By mastering the pipe symbol, you can create powerful pipelines of commands that can automate tasks and simplify your workflow. Remember to practice using pipes to become proficient in connecting commands.
