# The Relative and Absolute Permissions Changing Methods

## Introduction

UNIX systems have a unique approach to file permissions, which is based on a permission model that assigns access rights to users, groups, and other special users. Understanding how to change file permissions is an essential skill for any UNIX system programmer. In this document, we will explore the relative and absolute permissions changing methods, including historical context, modern developments, and applications.

## Historical Context

The UNIX file permission model dates back to the 1970s, when UNIX was first developed. The original permission model, known as the "octal permission system," used a three-digit octal number to represent the permissions. The first digit represented the owner's permissions, the second digit represented the group's permissions, and the third digit represented the other users' permissions. This system was simple and effective, but it had limitations.

In the 1980s, the UNIX permission model was extended to include additional permissions, such as sticky bits and executable bits. The permission model was also enhanced to support multiple users and groups.

## Relative Permissions

Relative permissions are a way to change file permissions without using the `chmod` command. Relative permissions are based on the file's existing permissions and are calculated by adding or subtracting a specific number of permissions.

### How Relative Permissions Work

Relative permissions work by modifying the file's permissions by a certain number of bits. The `chmod` command can be used to specify the number of bits to add or subtract. For example, if a file has read permissions for the owner and group, but not for other users, and you want to add read permissions for all users, you can use the following relative permission:

```bash
chmod 0666 file.txt
```

This will add 6 bits to the file's permissions, making it readable by all users.

### Types of Relative Permissions

There are two types of relative permissions:

- **Additive permissions**: These are used to add permissions to a file without removing any existing permissions. For example, `chmod 0666 file.txt` adds read permissions for all users.
- **Subtractive permissions**: These are used to remove permissions from a file. For example, `chmod 0444 file.txt` removes execute permissions for the owner and group.

## Absolute Permissions

Absolute permissions, on the other hand, are used to change the file's permissions without using relative permissions. Absolute permissions are based on a specific octal number that represents the file's permissions.

### How Absolute Permissions Work

Absolute permissions work by setting the file's permissions to a specific octal number. For example, if you want to set the file's permissions to read and write for the owner, group, and other users, you can use the following absolute permission:

```bash
chmod 0777 file.txt
```

This will set the file's permissions to read and write for the owner, group, and other users.

### Types of Absolute Permissions

There are three types of absolute permissions:

- **Owner permissions**: These are represented by the first digit of the octal number. For example, `chmod 0777 file.txt` sets the owner's permissions to read and write.
- **Group permissions**: These are represented by the second digit of the octal number. For example, `chmod 0777 file.txt` sets the group's permissions to read and write.
- **Other permissions**: These are represented by the third digit of the octal number. For example, `chmod 0777 file.txt` sets the other users' permissions to read and write.

## Applications

Relative and absolute permissions are used in a variety of applications, including:

- **File sharing**: Relative and absolute permissions can be used to grant access to shared files and directories.
- **Security**: Absolute permissions can be used to secure sensitive data by limiting access to specific users or groups.
- **Scripting**: Relative and absolute permissions can be used in scripting languages, such as Python and Perl, to automate tasks and manage files.

## Case Studies

### Case Study 1: File Sharing

Suppose you want to share a file with a group of users, but you don't want to grant them write access. You can use relative permissions to grant read access to the group, but not to the other users.

```bash
chmod 0644 shared_file.txt
```

This will grant read access to the group, but not to the other users.

### Case Study 2: Security

Suppose you want to secure a sensitive data file, but you still want to allow the owner and group to access it. You can use absolute permissions to grant limited access to the owner and group, but not to other users.

```bash
chmod 0700 sensitive_data.txt
```

This will grant read and write access to the owner and group, but not to other users.

## Diagram

Here is a diagram illustrating the relative and absolute permission model:

```
  +---------------+
  |  File Name    |
  +---------------+
           |
           |
           v
  +---------------+
  |  Permissions  |
  |  (octal)      |
  |  +---+---+---+  |
  |  |   |   |  |
  |  | u  | g  | o  |
  |  |---+---+---|  |
  |  |   |   |  |
  |  | r  | w  | r  |
  |  |---+---+---|  |
  |  |   |   |  |
  |  | x  | x  | x  |
  |  |---+---+---|  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Relative     |
  |  Permissions    |
  |  (chmod 0666)  |
  |  +---+---+---+  |
  |  |   |   |  |
  |  | u  | g  | o  |
  |  |---+---+---|  |
  |  |   |   |  |
  |  | r  | w  | r  |
  |  |---+---+---|  |
  |  |   |   |  |
  |  | x  | x  | x  |
  |  |---+---+---|  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Absolute    |
  |  Permissions  |
  |  (chmod 0777)  |
  |  +---+---+---+  |
  |  |   |   |  |
  |  | u  | g  | o  |
  |  |---+---+---|  |
  |  |   |   |  |
  |  | r  | w  | r  |
  |  |---+---+---|  |
  |  |   |   |  |
  |  | x  | x  | x  |
  |  |---+---+---|  |
  +---------------+
```

## Further Reading

- "UNIX Permissions" by Brian Kernighan and Dennis Ritchie
- "File Permissions" by Eric P. Peren
- "chmod" man page
- "The UNIX Programming Environment" by Brian Kernighan and Dennis Ritchie

In conclusion, the relative and absolute permissions changing methods are essential skills for any UNIX system programmer. Understanding how to use these methods can help you manage file permissions, share files, and secure sensitive data.
