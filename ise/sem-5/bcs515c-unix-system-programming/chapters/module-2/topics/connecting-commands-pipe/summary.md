# Connecting Commands: Pipe

### Definition and Purpose

- Pipe (`|`) is a command-line connector that redirects the output of one command as the input to another command.
- It allows for the creation of complex pipelines to perform multiple tasks in a single command.

### Key Points

- **Pipe syntax**: `command1 | command2`
- **Pipe order**: Commands are executed in the order they appear in the pipeline.
- **Pipe output**: The output of the first command becomes the input for the second command.
- **Redirection**: Pipes can be used with other redirection operators (e.g., `>`, `>>`, `<`).
- **Piping files**: Pipes can be used to pipe files from one command to another (e.g., `cat file1 | grep keyword`).

### Important Formulas and Definitions

- **Command pipelining**: A sequence of commands connected by pipes to achieve a specific task.
- **Input and output buffering**: Pipes can be used to optimize input and output buffering for commands.

### Important Theorems

- **The Pipe Theorem**: If a pipeline consists of `n` commands connected by pipes, the overall command has a time complexity of O(n).

### Revision Tips

- Practice writing complex pipelines to improve understanding of the pipe command.
- Use pipes to optimize file processing and command execution.
- Review the syntax and order of commands in a pipeline to ensure correct execution.
