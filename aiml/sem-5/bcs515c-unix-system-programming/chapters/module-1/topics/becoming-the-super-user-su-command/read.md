# Becoming the Super User: su Command

## **Introduction**

As a beginner in UNIX system programming, it's essential to understand the concept of super user and how to become one. The super user, also known as the root user, has administrative privileges and can modify system settings, install software, and perform other tasks that require elevated access. In this study material, we'll explore the `su` command, which allows users to become the super user.

## **What is Super User?**

The super user, also known as the root user, has the highest level of access and privileges on a system. The root user has the ability to:

- Modify system settings
- Install software
- Create and manage user accounts
- Edit system configuration files
- Perform other administrative tasks

## **What is su Command?**

The `su` command is a utility that allows users to switch to another user account. The `su` command can be used to become the super user, giving the user administrative privileges. The general syntax of the `su` command is:

```bash
su [options] [username]
```

## **Options:**

Here are the common options used with the `su` command:

- `-`
- `-c`
- `-p`
- `-s`
- `-t`

## **-**

The `-` option is used to become the super user. When this option is used, the user is prompted to enter the password of the super user account.

```bash
su - [username]
```

## **-c**

The `-c` option is used to execute a command as the super user. The command is specified after the options.

```bash
su -c "command" [username]
```

## **-p**

The `-p` option is used to use the default shell of the super user account. This option is useful when you want to switch to the super user account without being prompted for a password.

```bash
su -p [username]
```

## **-s**

The `-s` option is used to specify the shell that you want to use when becoming the super user. This option is useful when you want to switch to the super user account using a different shell.

```bash
su -s [shell] [username]
```

## **-t**

The `-t` option is used to set up an interactive shell for the super user account. This option is useful when you want to switch to the super user account and interact with the system using an interactive shell.

```bash
su -t [username]
```

## **Example Usage**

Here are some examples of using the `su` command:

```bash
# Become the super user using the default shell
su -

# Become the super user using the default shell and execute a command
su -c "ls -l"

# Become the super user using the default shell and specify the shell
su -s /bin/bash

# Become the super user using the default shell and set up an interactive shell
su -t
```

## **Best Practices**

Here are some best practices to keep in mind when using the `su` command:

- Always use the `-` option when becoming the super user.
- Be careful when using the `su` command, as it can potentially compromise system security.
- Use the `su` command only for legitimate administrative tasks.
- Always switch back to your original user account after completing administrative tasks.

By following these guidelines and using the `su` command correctly, you can become a super user and perform administrative tasks on your UNIX system.
