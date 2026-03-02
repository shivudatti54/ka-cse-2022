# **Basic Unix Commands**

### 1.1 Introduction

In this section, we will cover the basic Unix commands that are used to interact with the operating system and perform various tasks.

### 1.2 Echo Command

The `echo` command is used to display text on the screen.

#### Syntax

```bash
echo [options] 'string'
```

#### Options

- `-n`: Do not print a newline at the end of the output.
- `-e`: Interpret backslash escapes in the string.
- `-e` is not a standard option and is specific to some systems.

#### Example

```bash
echo "Hello World!"
```

This will display the text "Hello World!" on the screen.

```bash
echo -n "Hello World!"
```

This will display the text "Hello World!" on the screen without a newline at the end.

### 1.3 Print Command

The `printf` command is used to format and display text on the screen.

#### Syntax

```bash
printf [options] format [arguments...]
```

#### Options

- `%s`: Display the string as is.
- `%d`: Display the integer as a decimal number.
- `%x`: Display the integer as a hexadecimal number.
- `%f`: Display the floating-point number as a floating-point number.

#### Example

```bash
printf "The answer is %d\n" 42
```

This will display the text "The answer is 42" on the screen.

```bash
printf "The answer is %x\n" 42
```

This will display the text "The answer is a2" on the screen.

### 1.4 List Command

The `ls` command is used to list files and directories in the current directory.

#### Syntax

```bash
ls [options] [file...]
```

#### Options

- `-a`: Display all files, including hidden files.
- `-l`: Display a detailed list of files and directories.
- `-r`: Reverse the order of the list.

#### Example

```bash
ls
```

This will display a list of files and directories in the current directory.

```bash
ls -l
```

This will display a detailed list of files and directories in the current directory.

### 1.5 Who Command

The `who` command is used to display information about the current user.

#### Syntax

```bash
who
```

#### Example

```bash
who
```

This will display the following information:

- `username`: The username of the current user.
- `login`: The login time of the current user.
- `id`: The ID of the current user.
- ` terminal`: The terminal type of the current user.

### 1.6 Date Command

The `date` command is used to display the current date and time.

#### Syntax

```bash
date [options]
```

#### Options

- `+`: Add a specified number of days to the current date.
- `-d`: Display a specified date.
- `-r`: Display a relative date.

#### Example

```bash
date
```

This will display the current date and time.

```bash
date -d "2022-01-01"
```

This will display the date "2022-01-01".

### 1.7 Password Command

The `passwd` command is used to change the password of the current user.

#### Syntax

```bash
passwd [options] newpassword
```

#### Options

- `-p`: Specify a new password.
- `-m`: Specify a minimum password length.
- `-l`: Specify a maximum password length.

#### Example

```bash
passwd
```

This will prompt the user to enter a new password.

```bash
passwd -m 8
```

This will prompt the user to enter a new password with a minimum length of 8 characters.

### 1.8 Cal Command

The `cal` command is used to display a calendar for the current month.

#### Syntax

```bash
cal [month] [year]
```

#### Example

```bash
cal
```

This will display a calendar for the current month.

### 1.9 Combining Commands

Unix commands can be combined using the pipe (`|`) operator to pipe the output of one command as the input to another command.

#### Example

```bash
ls -l | grep keyword
```

This will display a list of files and directories that match the specified keyword.

### 1.10 Conclusion

In this section, we covered the basic Unix commands that are used to interact with the operating system and perform various tasks. We also covered how to combine commands using the pipe operator.

### 1.11 Practice Exercises

1. Use the `echo` command to display a message on the screen.
2. Use the `printf` command to display a formatted message on the screen.
3. Use the `ls` command to list files and directories in the current directory.
4. Use the `who` command to display information about the current user.
5. Use the `date` command to display the current date and time.
6. Use the `passwd` command to change the password of the current user.
7. Use the `cal` command to display a calendar for the current month.
8. Use the pipe operator to combine two or more commands to perform a task.
