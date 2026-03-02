# **The Relative and Absolute Permissions Changing Methods**

## **Introduction**

In UNIX system programming, file permissions play a crucial role in controlling access to files and directories. Permissions allow users to read, write, and execute files, and they can be modified using the `chmod` command. There are two types of permission changing methods: relative and absolute. In this study material, we will explore both methods, including their definitions, explanations, examples, and key concepts.

## **Relative Permissions Changing Methods**

Relative permissions changing methods are used to modify the file permissions based on the current user, group, and other permissions. The `chmod` command uses the following syntax:

```
chmod [permissions] [file_name]
```

## **Types of Relative Permissions**

- **u** (user): Modifies the permissions for the current user.
- **g** (group): Modifies the permissions for the current group.
- **o** (other): Modifies the permissions for others (users outside the current group and user).

## **Example: Modifying File Permissions with Relative Permissions**

Suppose we have a file `example.txt` with the following permissions:

```
-rwxr-xr-x
```

To modify the file permissions to:

```
-rwxr-w-rx
```

We can use the following `chmod` command:

```
chmod u+w,g-w,o+w example.txt
```

This command modifies the permissions as follows:

- `u+w`: Adds write permission for the current user.
- `g-w`: Removes write permission for the current group.
- `o+w`: Adds write permission for others.

## **Absolute Permissions Changing Methods**

Absolute permissions changing methods are used to modify the file permissions directly, without considering the current user, group, or other permissions. The `chmod` command uses the following syntax:

```
chmod [permissions] [file_name]
```

## **Types of Absolute Permissions**

- **u**: Modifies the permissions for the current user.
- **g**: Modifies the permissions for the current group.
- **o**: Modifies the permissions for others (users outside the current group and user).
- **a**: Modifies the permissions for all (current user, group, and others).

## **Example: Modifying File Permissions with Absolute Permissions**

Suppose we have a file `example.txt` with the following permissions:

```
-rwxr-xr-x
```

To modify the file permissions to:

```
-rwxrwxrwx
```

We can use the following `chmod` command:

```
chmod 777 example.txt
```

This command modifies the permissions as follows:

- `u` (owner): `rwx` (read, write, execute)
- `g` (group): `rwx` (read, write, execute)
- `o` (other): `rwx` (read, write, execute)

## **Key Concepts**

- **Base 8**: File permissions are represented using a base 8 system, where each digit represents a permission (read, write, execute).
- **Octal Notation**: The `chmod` command uses octal notation to specify permissions.
- **File Type**: The `chmod` command can be used to modify the file type (e.g., from regular file to directory).

## **Best Practices**

- Use the `chmod` command to modify file permissions.
- Use octal notation to specify permissions.
- Be careful when modifying file permissions, as incorrect permissions can lead to unauthorized access.

By understanding the relative and absolute permissions changing methods, you can effectively manage file permissions in UNIX system programming.
