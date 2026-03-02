# Shell Programming: Ordinary and Environment Variables

## Introduction

Shell programming is a fundamental aspect of UNIX system programming, and understanding ordinary and environment variables is crucial for any aspiring UNIX system programmer. In this document, we will delve into the world of shell variables, exploring their history, types, usage, and applications.

## History of Shell Variables

The concept of shell variables dates back to the early days of UNIX, when the shell was a simple text-based interface to the operating system. The first shell, called the "shell script," was written in 1971 by Ken Thompson and Dennis Ritchie. Initially, shell variables were used to store and manipulate command-line arguments and options.

Over time, the concept of shell variables evolved to include environment variables, which were introduced in the UNIX 7th edition (1980). Environment variables allowed programs to access and manipulate variables that were set by the shell or other programs, rather than just being limited to command-line arguments.

## Types of Shell Variables

There are two types of shell variables: ordinary variables and environment variables.

### Ordinary Variables

Ordinary variables are declared within a shell script using the `varName` syntax. They are local to the script and are not accessible from outside the script.

```bash
my_var= "Hello, World!"
echo $my_var
```

### Environment Variables

Environment variables are declared using the `export` command or by setting a variable in the shell configuration file (e.g., `~/.bashrc`). They are accessible from anywhere in the system and can be used by programs to store and manipulate data.

```bash
export MY_VAR="Hello, World!"
echo $MY_VAR
```

### Variables in the Shell Configuration File

Variables can also be set in the shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`). These variables are available to all shell sessions and can be used to customize the shell's behavior.

```bash
echo "export EDITOR=vim" >> ~/.bashrc
source ~/.bashrc
```

## Types of Environmental Variables

There are several types of environmental variables:

- **Path Variables**: Store directory paths used by the system.
- **User Variables**: Store user-specific information.
- **System Variables**: Store system-wide information.

## Path Variables

Path variables are used to store directory paths used by the system. They are typically set in the `/etc/environment` file and are accessible to all users.

```bash
export PATH=$PATH:/usr/local/bin
```

## User Variables

User variables are used to store user-specific information. They are typically set in the `~/.bashrc` file and are accessible to the user.

```bash
export HOME=/home/user
```

## System Variables

System variables are used to store system-wide information. They are typically set in the `/etc/environment` file and are accessible to all users.

```bash
export HOSTNAME=localhost
```

## Accessing and Modifying Environmental Variables

There are several ways to access and modify environmental variables:

- **Environment Variables in the Command Line**: Environment variables can be accessed in the command line using the `$` symbol.

      ```bash

  echo $PATH

````

*   **Environment Variables in a Shell Script**: Environment variables can be accessed in a shell script using the `export` command.

    ```bash
#!/bin/bash
export MY_VAR="Hello, World!"
echo $MY_VAR
````

- **Environment Variables in the Shell Configuration File**: Environment variables can be set in the shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`).

      ```bash

  echo "export EDITOR=vim" >> ~/.bashrc
  source ~/.bashrc

````

*   **Printing Environmental Variables**: Environmental variables can be printed using the `echo` command.

    ```bash
echo $PATH
echo $HOME
````

## Applications of Environmental Variables

Environmental variables have numerous applications in UNIX programming:

- **Configuring Shell Scripts**: Environmental variables can be used to customize shell scripts and make them more flexible.

      ```bash

  #!/bin/bash
  export MY_VAR="Hello, World!"
  echo $MY_VAR

````

*   **Customizing Shell Behavior**: Environmental variables can be used to customize shell behavior and make it more user-friendly.

    ```bash
echo "export EDITOR=vim" >> ~/.bashrc
source ~/.bashrc
````

- **Managing Files and Directories**: Environmental variables can be used to manage files and directories.

      ```bash

  export HOME=/home/user
  echo $HOME

````

Case Study: Using Environmental Variables in a UNIX System
---------------------------------------------------------

Suppose we are building a UNIX system that needs to manage user-specific configuration files. We can use environmental variables to store the user's home directory and other configuration settings.

```bash
#!/bin/bash
export HOME=$HOME
export EDITOR=vim
echo $HOME
echo $EDITOR
````

In this example, we use environmental variables to store the user's home directory and editor settings. The `export` command makes these variables available to all shell sessions.

## Conclusion

In conclusion, shell programming is a fundamental aspect of UNIX system programming, and understanding ordinary and environment variables is crucial for any aspiring UNIX system programmer. Environmental variables are used to store and manipulate data that is accessible to all shell sessions. They have numerous applications in UNIX programming, including configuring shell scripts, customizing shell behavior, and managing files and directories.

**Further Reading**

- "The UNIX Programming Environment" by Brian Kernighan and Dennis Ritchie
- "Advanced UNIX Programming" by Richard McDougall
- "The Art of Shell Scripting" by Mick Nelson
- "Linux System Administration" by Martin R. Powell
