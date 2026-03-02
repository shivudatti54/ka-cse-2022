### Revision Notes: Basic Unix Commands

=============================================

### Introduction

---

- Unix is a multi-user, multi-tasking operating system.
- It is based on the concept of a pipeline and filters.

### Basic Unix Commands

---

### I. Path and File Commands

- `echo`: prints its argument to the standard output.
  - Syntax: `echo [options] 'string'`
  - Example: `echo "Hello World!"`
- `printf`: prints formatted output to the standard output.
  - Syntax: `printf [options] format_string`
  - Example: `printf "%d %s\n" 10 "Hello"`
- `ls`: lists the files and directories in the current directory.
  - Syntax: `ls [options] [file_name]`
  - Example: `ls -l`

### II. User and Password Commands

- `who`: displays information about the current user.
  - Syntax: `who`
  - Example: `whoami`
- `date`: displays the current date and time.
  - Syntax: `date [options]`
  - Example: `date +%Y-%m-%d`
- `passwd`: displays or changes the password for a user.
  - Syntax: `passwd [options]`
  - Example: `passwd -p`
- `cal`: displays a calendar for a given month and year.
  - Syntax: `cal [options] [month] [year]`
  - Example: `cal -y 2024`

### III. Combining Commands

- Command pipes (`|`): allows you to chain commands together.
  - Example: `ls -l | grep keyword`
- Command redirection (`>` and `<`): allows you to redirect output to files or input from files.
  - Example: `ls > output.txt` and `cat output.txt`

### Key Formulas and Definitions

---

- None

### Important Theorems

---

- None

### Revision Tips

---

- Practice using the commands to improve your skills.
- Use online resources or books for reference.
- Focus on the syntax and options for each command.
