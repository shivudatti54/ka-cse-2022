# **Shell Programming: Ordinary and Environment Variables**

## **Introduction**

In shell programming, variables play a crucial role in storing and manipulating data. There are two types of variables in shells: ordinary variables and environment variables. In this topic, we will explore the differences between these two types of variables, their usage, and examples.

## **Ordinary Variables**

An ordinary variable is a shell variable that is defined and used within a specific shell script or command. These variables are not persistent across different shell sessions and are deleted when the shell script or command terminates.

### Characteristics of Ordinary Variables

- **Scope**: Local to the shell script or command
- **Lifetime**: Temporary, deleted when the shell script or command terminates
- **Access**: Can be accessed within the shell script or command where they are defined

### Examples of Ordinary Variables

```bash
# Define an ordinary variable
MY_VAR="Hello, World!"

# Print the value of the ordinary variable
echo $MY_VAR
```

## **Environment Variables**

An environment variable is a shell variable that is defined and used across different shell sessions. These variables are persistent and can be accessed from any shell session.

### Characteristics of Environment Variables

- **Scope**: Global, accessible across different shell sessions
- **Lifetime**: Persistent, retains its value across shell sessions
- **Access**: Can be accessed from any shell session where the variable is set

### Examples of Environment Variables

```bash
# Set an environment variable
export MY_VAR="Hello, World!"

# Print the value of the environment variable
echo $MY_VAR
```

## **Setting Environment Variables**

Environment variables can be set in several ways:

- **Local variables**: Set using the `export` command within a shell script or command
- **System-wide variables**: Set using the `export` command in the shell's startup file (e.g., `~/.bashrc`)
- **Environment file**: Set using an environment file (e.g., `/etc/environment`)

## **Accessing Environment Variables**

Environment variables can be accessed using the `$` symbol or the `export` command.

### Examples of Accessing Environment Variables

```bash
# Access an environment variable using the $ symbol
echo $MY_VAR

# Access an environment variable using the export command
export MY_VAR="New Value!"
echo $MY_VAR
```

## **Best Practices for Using Ordinary and Environment Variables**

- Use ordinary variables for short-lived data that is specific to a shell script or command.
- Use environment variables for persistent data that is shared across different shell sessions.

By following these guidelines and examples, you can effectively use ordinary and environment variables in your shell programming projects.
