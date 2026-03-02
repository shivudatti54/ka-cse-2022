# General Features of Unix Commands/ Command Structure

=====================================================

### Overview

- Unix commands are used to interact with the operating system and perform various tasks.
- The command structure is based on the concept of a pipe, redirection, and command substitution.

### Key Features

- **Command Line Interface (CLI)**:
  - A text-based interface for interacting with the operating system.
  - Used to execute commands and provide input.
- **Command Structure**:
  - Command + Option + Argument = Command Line
  - Command line arguments can be:
    - Options (e.g., -l, -a)
    - Arguments (e.g., file name)
- **Pipe (|)**:
  - Redirects the output of one command as input to another command.
  - Used to chain commands together.
- **Redirection**:
  - Used to redirect the output of a command to a file or another command.
  - Commonly used with the redirection operators:
    - > (output redirection)
    - < (input redirection)
- **Command Substitution**:
  - Used to substitute the output of a command into another command.
  - Often used with the `$( )` syntax or the `let` command.
- **File Permissions**:
  - Used to control access to files and directories.
  - Governed by the file mode bits ( permissions bits of a file's mode).
- **Command History**:
  - Used to recall and execute previous commands.
  - Often bound to a key combination (e.g., Ctrl+R).

### Important Formulas/ Definitions/Theorems

- None specific to Unix commands, but relevant to Unix system programming:
  - Unix file system hierarchy
  - Unix process creation and management (e.g., fork, exec, wait)
  - Unix signal handling (e.g., signal, kill)
