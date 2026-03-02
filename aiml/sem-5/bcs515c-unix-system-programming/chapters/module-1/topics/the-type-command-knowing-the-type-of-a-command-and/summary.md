# **The type command: Knowing the type of a command and locating it**

### Overview

---

- The `type` command in UNIX is used to determine the type of a command and locate it.
- It displays information about a command, including its type (binary, shell, kernel, etc.) and location.

### Key Points

---

- **Syntax:**
  - `type [command]`
- **Output:**
  - `file` type (e.g., binary, shell, kernel)
  - `path` to the command (if located)
  - `script` type (if a shell script)

### Formulae and Definitions

---

- None

### Theorems

---

- The `type` command is not affected by the environment, so it will always display the correct type of a command, regardless of the current working directory.
- The `type` command can be used to identify if a command is a shell script or a binary.

### Examples

---

- `type ls` - displays the type of the `ls` command and its location.
- `type script` - displays the type of a script.

### Revision Tips

---

- Practice using the `type` command with different commands to become familiar with its syntax and output.
- Review the different types of commands and their characteristics.
