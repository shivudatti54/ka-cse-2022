# Shell Programming: Ordinary and Environment Variables

## Introduction

Shell programming is a fundamental aspect of UNIX system programming, allowing users to automate tasks and interact with the operating system. In this section, we will delve into the world of shell programming, focusing on ordinary and environment variables. Understanding these concepts is crucial for any UNIX system programmer, as they enable you to customize and extend the shell to suit your needs.

## History

The concept of variables in shell programming dates back to the early days of UNIX. In the late 1970s, Bill Joy, one of the creators of UNIX, introduced the concept of variables in the shell. The first shell, called the Bourne shell (sh), was written by Stephen Bourne in 1977. It introduced the `export` command, which allowed users to set environment variables.

In the 1980s, the C shell (csh) was developed, which added more features to the shell, including the ability to set variables using the `set` command. The Bourne shell, on the other hand, used the `export` command to set variables.

Today, shell programming is a vital skill for any UNIX system programmer, and understanding ordinary and environment variables is essential for customizing and extending the shell.

## Ordinary Variables

Ordinary variables, also known as shell variables, are variables that are set and used within a shell session. They are local to the shell and are not stored anywhere on disk. Ordinary variables are useful for storing temporary values or intermediate results.

## Types of Ordinary Variables

There are two types of ordinary variables:

- **Local variables**: These variables are set and used within a shell script or interactive shell session.
- **Global variables**: These variables are set in a shell script and can be accessed from any other shell script.

## Setting Ordinary Variables

Ordinary variables can be set using the following methods:

- **Assignment operator (`=`)**: Assign a value to a variable using the assignment operator.
- **`export` command**: Set a variable and make it available to all child processes.

Example:

```bash
# Set a local variable
MY_VAR=hello

# Print the value of the variable
echo $MY_VAR

# Set a global variable using export
export MY_GLOBAL_VAR=world
```

## Environment Variables

Environment variables are variables that are set on the system level and are available to all shell sessions. They are stored in the `/etc/environment` file and are used to configure the system. Environment variables are useful for storing system-wide settings and configuration.

## Types of Environment Variables

There are two types of environment variables:

- **System variables**: These variables are set in the `/etc/environment` file and are available to all shell sessions.
- **User variables**: These variables are set in the user's shell configuration file (`~/.bashrc` or `~/.bash_profile`) and are only available to the user's shell session.

## Setting Environment Variables

Environment variables can be set using the following methods:

- **`export` command**: Set a variable and make it available to all child processes.
- **`export -e` command**: Set a variable and make it available to all shell sessions.

Example:

```bash
# Set a system variable using export
export MY_SYSTEM_VAR=hello

# Set a user variable using export
export -e MY_USER_VAR=world
```

## Accessing Environment Variables

Environment variables can be accessed using the `$` symbol or the `${parameter}` syntax.

Example:

```bash
# Print the value of an environment variable
echo $MY_SYSTEM_VAR

# Print the value of an environment variable using the ${parameter} syntax
echo ${MY_USER_VAR}
```

## Case Study: Customizing the Shell

In this case study, we will show how to customize the shell by setting ordinary and environment variables.

**Goal:** Set up a customized shell environment with a specific set of variables.

**Step 1:** Set up the shell configuration file (`~/.bashrc` or `~/.bash_profile`)

Add the following lines to the shell configuration file:

```bash
# Set a customized variable
MY_CUSTOM_VAR="Hello, World!"

# Print the value of the customized variable
echo $MY_CUSTOM_VAR
```

**Step 2:** Set up environment variables

Add the following lines to the environment variables file (`/etc/environment` or `~/.bashrc`):

```bash
# Set a system variable
MY_SYSTEM_VAR="Hello, System!"

# Set a user variable
export -e MY_USER_VAR="Hello, User!"
```

**Step 3:** Run the shell

Run the shell and verify that the customized variables are set.

Example:

```bash
# Run the shell
bash

# Print the value of the customized variable
echo $MY_CUSTOM_VAR

# Print the value of the system variable
echo $MY_SYSTEM_VAR

# Print the value of the user variable
echo ${MY_USER_VAR}
```

## Conclusion

In this section, we have explored the concepts of ordinary and environment variables in shell programming. We have discussed the history, types, and setting of ordinary variables, as well as environment variables. We have also provided examples and a case study on customizing the shell using ordinary and environment variables.

## Further Reading

- **"The Bourne Shell Command Line Reference"**: A comprehensive reference manual for the Bourne shell.
- **"The C Shell Reference Manual"**: A comprehensive reference manual for the C shell.
- **"UNIX System Administration Handbook"**: A comprehensive guide to UNIX system administration.
- **"Shell Scripting with Bash"**: A comprehensive guide to shell scripting with Bash.

## Diagram: Shell Variables

[Diagram: Shell Variables]

```
+-----------------------+
|  Ordinary Variables  |
+-----------------------+
|  Local Variables   |
|  Global Variables  |
+-----------------------+
|  Environment Variables  |
|  System Variables    |
|  User Variables     |
+-----------------------+
```

This diagram illustrates the relationship between ordinary and environment variables in shell programming.
