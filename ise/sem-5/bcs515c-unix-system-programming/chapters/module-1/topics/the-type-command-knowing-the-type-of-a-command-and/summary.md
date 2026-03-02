# **UNIX SYSTEM PROGRAMMING**

# **Topic: The type command: knowing the type of a command and locating it**

### Key Points

- **Purpose of `type` command**:
  - To determine the type of a command (builtin, script, or executable)
  - To locate a command
- **Options**:
  - `-a` : display all types of files
  - `-t` : display only the type of a file
  - `-A` : display all types of files in a specified directory
  - `-T` : display only the type of files in a specified directory
- **Examples**:
  - `type -a bash` : displays all types of the `bash` command
  - `type -t ls` : displays the type of the `ls` command
  - `type -A /bin` : displays all types of files in the `/bin` directory
  - `type -T /bin` : displays only the types of files in the `/bin` directory

### Formulas, Definitions, and Theorems

- None

### Important UNIX Commands

- `type` command
- `which` command (alternative to `type` for locating a command)

### Revision Tips

- Practice using the `type` command with different options and examples
- Review the differences between `builtin`, `script`, and `executable` types
- Familiarize yourself with the `which` command as an alternative to `type`
