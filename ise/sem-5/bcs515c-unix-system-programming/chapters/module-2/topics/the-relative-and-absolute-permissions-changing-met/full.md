# **The Relative and Absolute Permissions Changing Methods**

## **Introduction**

In UNIX system programming, file permissions play a crucial role in controlling access to files and directories. Permissions determine what actions a user can perform on a file or directory, such as reading, writing, or executing. In this topic, we will explore two methods of changing file permissions: relative and absolute.

## **Historical Context**

The concept of file permissions dates back to the early days of UNIX. In 1971, Bell Labs developed the UNIX operating system, which introduced the concept of permissions in the form of access control lists (ACLs). ACLs allowed system administrators to specify permissions for each user and group.

Over time, the file permission system evolved to include the concept of modes, which are used to determine the permissions of a file or directory. The current file permission system is based on the Unix File System (UFS) and the Network File System (NFS).

## **File Permission Modes**

File permission modes are represented by three digits, each corresponding to the permissions for the owner, group, and other users, respectively. The modes are defined as follows:

- `r` (read): the file can be read by the user
- `w` (write): the file can be written to by the user
- `x` (execute): the file can be executed by the user
- `-` (no permission): the user has no permission

The file permission modes are represented in hexadecimal notation using the following values:

- `rwx` = 7 (0007)
- `rw-` = 6 (0006)
- `r-x` = 5 (0005)
- `-w-` = 2 (0002)
- `-wx` = 1 (0001)
- `-r--` = 4 (0004)

## **Relative Permissions Changing Methods**

Relative permissions changing methods involve changing the permissions of a file or directory with respect to its current permissions. There are two types of relative permissions changing methods:

### 1. Using the `chmod` Command

The `chmod` command is used to change the file permissions of a file or directory. The basic syntax of the `chmod` command is as follows:

```bash
chmod [mode] [file_name]
```

For example, to change the permissions of a file to read and write, but not execute, you can use the following command:

```bash
chmod 644 file.txt
```

This command sets the permissions of the file to read and write for the owner, but not execute, and read for the group and other users.

### 2. Using the `chown` Command

The `chown` command is used to change the ownership of a file or directory. The `chown` command can also be used to change the permissions of a file or directory by specifying the new permissions.

For example, to change the ownership of a file to a different user and set the permissions to read and write for the owner, but not execute, you can use the following command:

```bash
chown user:group file.txt
chmod 644 file.txt
```

### 3. Using the `chgrp` Command

The `chgrp` command is used to change the group ownership of a file or directory. The `chgrp` command can also be used to change the permissions of a file or directory by specifying the new permissions.

For example, to change the group ownership of a file to a different group and set the permissions to read and write for the owner, but not execute, you can use the following command:

```bash
chgrp group file.txt
chmod 644 file.txt
```

## **Absolute Permissions Changing Methods**

Absolute permissions changing methods involve changing the permissions of a file or directory without considering the current permissions.

### 1. Using the `drwxr-xr-x` Permission Mode

The `drwxr-xr-x` permission mode is an absolute permission mode that sets the permissions of a directory as follows:

- `d` (directory): the directory can be read and executed by the owner, read and executed by the group, and read by other users
- `r` (read): the directory can be read by the owner, read by the group, and read by other users
- `w` (write): the directory can be written to by the owner, written to by the group, and written to by other users
- `x` (execute): the directory can be executed by the owner, executed by the group, and executed by other users

For example, to create a directory with the `drwxr-xr-x` permission mode, you can use the following command:

```bash
mkdir -m 755 directory_name
```

### 2. Using the `chown` Command with Absolute Permissions

When using the `chown` command to change the ownership of a file or directory, you can specify absolute permissions by using the `--mode` option.

For example, to change the ownership of a file to a different user and set the permissions to read and write for the owner, but not execute, you can use the following command:

```bash
chown user:group file.txt --mode=644
```

## **Case Study: Access Control**

In this case study, we will demonstrate the use of absolute and relative permissions changing methods to control access to files and directories.

Let's assume that we have a file called `secret.txt` that contains sensitive information. We want to control access to this file to ensure that only authorized users can read or write to it.

We can create the file with the `drwxr-x-----` permission mode to limit access to only the owner and the group that we specify:

```bash
mkdir -m 700 secret_directory
touch -m 600 secret.txt
```

In this example, the `drwxr-x-----` permission mode sets the permissions of the `secret_directory` as follows:

- `d` (directory): the directory can be read and executed by the owner and the group, but not by other users
- `r` (read): the directory can be read by the owner and the group, but not by other users
- `w` (write): the directory can be written to by the owner and the group, but not by other users
- `x` (execute): the directory can be executed by the owner and the group, but not by other users

The `600` permission mode sets the permissions of the `secret.txt` file as follows:

- `r` (read): the file can be read by the owner, read by the group, and read by other users
- `w` (write): the file can be written to by the owner, written to by the group, and written to by other users
- `x` (execute): the file cannot be executed by the owner, group, or other users

## **Applications**

File permissions changing methods have various applications in UNIX system programming. Some of the applications include:

- **Security**: file permissions can be used to control access to sensitive information, such as passwords or confidential data.
- **Data confidentiality**: file permissions can be used to protect data from unauthorized access.
- **Data integrity**: file permissions can be used to ensure that data is not modified or deleted by unauthorized users.
- **Resource allocation**: file permissions can be used to manage resource allocation, such as allocating resources to users or groups.

## **Conclusion**

In this topic, we explored the relative and absolute permissions changing methods in UNIX system programming. We discussed the history of file permissions, the file permission modes, and the relative and absolute permissions changing methods. We also provided examples and case studies to demonstrate the use of file permissions changing methods in various applications.

## **Further Reading**

- UNIX File System (UFS)
- Network File System (NFS)
- Access Control Lists (ACLs)
- UNIX permissions
- File attribute and permissions
- UNIX system programming
- UNIX file system permissions

References:

- UNIX (1971). Bell Labs.
- UNIX File System (UFS) (1983). UNIX System Laboratories.
- Network File System (NFS) (1984). UNIX System Laboratories.
- Access Control Lists (ACLs) (1990). UNIX System Laboratories.
- UNIX permissions (1990). UNIX System Laboratories.
- UNIX file system permissions (1990). UNIX System Laboratories.

Note: The references provided are for historical purposes only and may not be up-to-date or accurate.
