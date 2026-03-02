# Environment Variables in Linux/Unix

## Introduction

Environment variables are dynamic values that affect the behavior of processes running in an operating system. They form a fundamental concept in Linux/Unix systems, serving as the backbone for system configuration, application behavior, and shell customization. For CSE students studying Operating Systems or Unix/Linux programming, understanding environment variables is essential as they control how programs access system resources, locate files, and communicate with the kernel.

In the Linux ecosystem, every process inherits a set of environment variables from its parent process, creating a hierarchical information-passing mechanism. This inheritance allows system administrators and users to configure system-wide behaviors without modifying program code. Environment variables are extensively used in shell scripting, program compilation, software installation, and system administration tasks. Major software applications like compilers, database systems, and web servers heavily rely on environment variables for their configuration and operation.

The concept of environment variables becomes particularly important when working with the bash shell, as it provides extensive support for creating, modifying, and utilizing these variables. Whether you are setting up a development environment, configuring system paths, or writing automation scripts, environment variables play a pivotal role in determining how the system behaves.

## Key Concepts

### Definition and Nature of Environment Variables

Environment variables are name-value pairs stored in a special memory area that the operating system maintains for each process. Unlike regular variables in programming languages, environment variables are inherited by child processes, making them ideal for passing configuration information across process hierarchies. The environment is represented as a character pointer array (environ) in Unix systems, where each entry follows the format "NAME=value".

Environment variables can be categorized into three main types: **system environment variables** that are defined by the operating system and apply globally to all users, **user environment variables** that are specific to individual user accounts and defined in user configuration files, and **shell variables** that exist only within the current shell session and are not inherited by child processes.

### Common Environment Variables

The most frequently used environment variable is **PATH**, which contains a colon-separated list of directories that the shell searches for executable files. When you type a command like 'ls' or 'gcc', the shell searches each directory listed in PATH to find the corresponding executable. The **HOME** variable stores the path to the current user's home directory, used by various commands and applications for locating user-specific configuration files.

Other important environment variables include **SHELL** (specifies the default shell for the user), **USER** (current username), **PWD** (current working directory), **LANG** (default language and locale settings), **TERM** (terminal type for applications requiring terminal information), and **DISPLAY** (X Window System display identifier). The **PS1** variable defines the primary prompt string in bash, while **PS2** defines the secondary prompt for multi-line commands.

### Shell Variables vs Environment Variables

A critical distinction exists between shell variables and environment variables in Linux. Shell variables are local to the current shell instance and are not passed to child processes, whereas environment variables are exported to child processes. When you assign a variable using `VAR=value`, it creates a shell variable. To convert it to an environment variable, you must use the `export` command: `export VAR=value`.

This distinction has practical implications. For example, if you set a variable in a shell script without exporting it, any command or script called from within that script will not have access to that variable. Understanding this difference is crucial for writing effective shell scripts and debugging variable-related issues.

### Configuration Files and Environment Variable Persistence

Environment variables can be set temporarily in the current session or made persistent across logins through configuration files. The common files for storing environment variable definitions include `/etc/environment` for system-wide variables, `/etc/profile` for system-wide login shell configurations, `~/.bashrc` for interactive non-login shells, `~/.bash_profile` or `~/.profile` for login shells, and `/etc/profile.d/` for modular system-wide configurations.

When bash starts, it reads these files in a specific order: first `/etc/profile`, then `~/.bash_profile`, `~/.bash_login`, or `~/.profile` (whichever exists first). The `~/.bashrc` file is sourced when starting an interactive non-login shell. This layering allows administrators to set system-wide defaults while users can override or extend them in their personal configuration files.

## Examples

### Example 1: Viewing and Setting Environment Variables

```bash
# View all environment variables
env
printenv

# View specific environment variable
echo $HOME
printenv PATH

# Set temporary environment variable (shell variable only)
MYVAR="hello"
echo $MYVAR

# Export variable to make it an environment variable
export MYVAR
# Or combine in one line
export MYVAR="hello"

# Verify export
bash -c 'echo $MYVAR' # This will print "hello"

# Without export, child process won't see it
NEWVAR="test"
bash -c 'echo $NEWVAR' # This will be empty
```

### Example 2: Adding a Directory to PATH

```bash
# View current PATH
echo $PATH

# Add a directory to PATH temporarily
export PATH=$PATH:/home/user/myprograms

# Verify the change
echo $PATH

# To make it permanent, add to ~/.bashrc
echo 'export PATH=$PATH:/home/user/myprograms' >> ~/.bashrc

# Reload the configuration
source ~/.bashrc

# Alternative approach using PATH manipulation
PATH="$PATH:/opt/android-sdk/tools:/opt/android-sdk/platform-tools"
export PATH
```

### Example 3: Creating a Custom Environment Variable for Development

```bash
# Create a development project structure
mkdir -p ~/dev/projects/myapp

# Set environment variables for the project
export PROJECT_HOME=~/dev/projects/myapp
export APP_PORT=8080
export APP_ENV=development
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Create a script that uses these variables
cat > ~/dev/projects/myapp/run.sh << 'EOF'
#!/bin/bash
echo "Starting $PROJECT_NAME on port $APP_PORT"
echo "Environment: $APP_ENV"
java -jar target/myapp.jar --server.port=$APP_PORT
EOF

chmod +x ~/dev/projects/myapp/run.sh

# Export for persistent use (add to ~/.bashrc)
cat >> ~/.bashrc << 'EOF'
# Project environment variables
export PROJECT_HOME=~/dev/projects/myapp
export PROJECT_NAME=myapp
export APP_PORT=8080
export APP_ENV=development
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
EOF

source ~/.bashrc
```

## Exam Tips

1. **Remember the key difference**: Shell variables are local to the current shell, while environment variables are inherited by child processes. Use `export` to convert shell variables to environment variables.

2. **Know common environment variables**: PATH, HOME, SHELL, USER, PWD, TERM, LANG are frequently asked in exams. Be able to explain the purpose of each.

3. **Understand configuration file order**: Remember that `/etc/profile` is executed first for login shells, followed by user-specific files like `~/.bash_profile` or `~/.profile`.

4. **Difference between source and execute**: When you run a script with `./script.sh`, it runs in a subshell. Using `source script.sh` or `. script.sh` executes in the current shell, preserving variables.

5. **PATH search mechanism**: When you type a command, the shell searches directories in PATH order from left to right and executes the first matching executable found.

6. **Persistent variable setup**: To make environment variables permanent, add them to `~/.bashrc` (for interactive shells) or `~/.bash_profile` (for login shells).

7. **Use printenv vs echo**: `printenv` displays environment variables without the $ prefix, while `echo $VARIABLE` requires the $ prefix. Both are used to view variables but have different syntax requirements.

8. **Practical commands**: Remember commands like `env` (list all environment variables), `printenv` (print environment variables), `export` (set environment variable), and `unset` (remove variable).

9. **PS1 and PS2**: PS1 defines the primary shell prompt (e.g., showing username, hostname, working directory), while PS2 is the continuation prompt (usually ">") for multi-line commands.

10. **Environment variable inheritance**: Child processes inherit a copy of the parent's environment, but changes in child processes do not affect the parent's environment.
