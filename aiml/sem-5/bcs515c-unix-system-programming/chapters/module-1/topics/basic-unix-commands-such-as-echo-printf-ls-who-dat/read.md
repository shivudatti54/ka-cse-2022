# **Basic Unix Commands**

### Table of Contents

1. [Echo Command](#echo-command)
2. [Printf Command](#printf-command)
3. [Ls Command](#ls-command)
4. [Who Command](#who-command)
5. [Date Command](#date-command)
6. [Passwd Command](#passwd-command)
7. [Cal Command](#cal-command)
8. [Combining Commands](#combining-commands)

### 1. Echo Command

The `echo` command is used to display text or commands on the screen. It is one of the most commonly used commands in Unix.

#### Syntax

`echo [options] [arguments]`

#### Options

- `-n` : suppresses the newline character at the end of the output
- `-e` : enables interpretation of backslash escapes
- `-e `: enables interpretation of backslash escape sequences
- `> ` : redirects output to a file

#### Example

```bash
echo "Hello World"
echo -n "Hello World"
echo -e "Hello\ World"
echo -e "Hello\ World" > output.txt
```

### 2. Printf Command

The `printf` command is used to format and print data. It is similar to the `echo` command but provides more formatting options.

#### Syntax

`printf [options] format_string [arguments]`

#### Options

- `-v` : allows a variable to be used in the format string
- `-l` : prints the format string in lowercase
- `-L` : prints the format string in uppercase
- `-e` : enables interpretation of backslash escapes
- `%` : used to specify the format

#### Example

```bash
printf "The answer is %d\n" 42
printf "%s is 42\n" "The answer"
printf "The answer is %d\n" "42"
```

### 3. Ls Command

The `ls` command is used to display a list of files and directories in the current directory.

#### Syntax

`ls [options] [arguments]`

#### Options

- `-a` : displays all files, including hidden files
- `-l` : displays a detailed list of files and directories
- `-r` : displays files in reverse chronological order
- `-d` : displays only directories
- `-A` : ignores the current and parent directories

#### Example

```bash
ls -l
ls -a
ls -r
ls -d .
ls -d ..
```

### 4. Who Command

The `who` command is used to display information about the users currently logged in to the system.

#### Syntax

`who [options]`

#### Options

- `-h` : displays a human-readable format
- `-c` : displays the login time for each user
- `-u` : displays the username instead of the login name
- `-n` : suppresses the newline character at the end of the output

#### Example

```bash
who
who -h
who -c
who -u
who -n
```

### 5. Date Command

The `date` command is used to display or manipulate the system date and time.

#### Syntax

`date [options] [arguments]`

#### Options

- `-d` : specifies a date and time
- `-l` : displays the date in a long format
- `-r` : displays the date in a relative format
- `-u` : displays the date in UTC time
- `-v` : displays the date in a verbose format

#### Example

```bash
date
date -l
date -r
date -u
date -v
```

### 6. Passwd Command

The `passwd` command is used to change the password of a user.

#### Syntax

`passwd [options] username`

#### Options

- `-n` : suppresses the prompt for the old password
- `-p` : specifies a new password
- `-r` : does not update the password history

#### Example

```bash
passwd user1
passwd -n user1
passwd -p user1
passwd -r user1
```

### 7. Cal Command

The `cal` command is used to display a calendar for a specified month and year.

#### Syntax

`cal [options] month year`

#### Options

- `-y` : sets the year
- `-m` : sets the month
- `-i` : displays the day of the week

#### Example

```bash
cal 2024 02
cal -y 2024 02
cal -m 02 2024
cal -i 2024 02
```

### 8. Combining Commands

Unix commands can be combined using various techniques, such as piping and redirection.

#### Piping

Piping is used to redirect the output of one command as the input to another command.

```bash
ls -l | grep keyword
```

#### Redirection

Redirection is used to redirect the output of a command to a file or pipe it to another command.

```bash
ls -l > output.txt
```

```bash
ls -l | grep keyword > output.txt
```

Combining commands can be used to automate tasks and simplify complex operations.
