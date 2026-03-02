# **The Relative and Absolute Permissions Changing Methods**

## **Introduction**

In UNIX systems, file permissions are a critical aspect of file management. Understanding how to change file permissions is essential for users, administrators, and developers. This study material covers two methods of changing file permissions: relative and absolute methods.

## **What are Permissions?**

Permissions refer to the rights granted to access and modify files. Each file has three types of permissions:

- Read permission (r): allows users to read the file contents.
- Write permission (w): allows users to modify or delete the file.
- Execute permission (x): allows users to execute the file as a program.

## **Relative Permissions**

Relative permissions refer to changing permissions using relative paths or symbolic links. This method involves using the `chmod` command with the `-R` option to recursively apply changes to a directory and its contents.

## **How to Change Relative Permissions**

To change relative permissions, use the `chmod` command with the `-R` option followed by the desired permissions.

```bash
chmod -R u+x /path/to/directory
```

- `u` specifies user permissions.
- `x` adds the execute permission for the user.

## **Example**

To add execute permissions to all files in the `/home/user/documents` directory and its contents, run the following command:

```bash
chmod -R u+x /home/user/documents
```

## **Absolute Permissions**

Absolute permissions refer to changing permissions using absolute paths or symbolic links. This method involves using the `chmod` command with the file path and the desired permissions.

## **How to Change Absolute Permissions**

To change absolute permissions, use the `chmod` command followed by the file path and the desired permissions.

```bash
chmod 755 /path/to/file
```

- `755` represents the file permissions: read (7), write (5), and execute (5) for the owner, group, and others, respectively.

## **Example**

To change the permissions of the `/home/user/documents/file.txt` file to read and write for the owner and group, but execute for others, run the following command:

```bash
chmod 644 /home/user/documents/file.txt
```

## **Key Concepts**

- `chmod` command: used to change file permissions.
- `-R` option: used to recursively apply changes to a directory and its contents.
- `u`, `g`, `o` options: used to specify user, group, and others permissions, respectively.
- `x`, `w`, `r` options: used to add or remove execute, write, and read permissions, respectively.

## **Best Practices**

- Use the `chmod` command with caution, as it can have unintended consequences.
- Use the `-R` option with extreme caution, as it can recursively change permissions for all files and directories in a given directory.
- Use absolute paths or symbolic links to ensure accurate permission changes.

By understanding the relative and absolute permissions changing methods, you can effectively manage file permissions in UNIX systems. Remember to use the `chmod` command with caution and consider the consequences of your actions.
