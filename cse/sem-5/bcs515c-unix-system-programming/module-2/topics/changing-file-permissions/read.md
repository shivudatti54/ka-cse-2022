# Changing File Permissions in Linux/Unix

## Introduction

File permissions are a fundamental aspect of security in Linux and Unix-based operating systems. Every file and directory in these systems has an associated set of permissions that determine who can read, write, or execute them. Understanding how to change these permissions is crucial for any system administrator or developer working with Linux systems. This knowledge is essential not only for securing sensitive files but also for proper configuration of web servers, application deployment, and multi-user system management.

In the context of 's Computer Science and Engineering curriculum, this topic forms a critical component of Operating Systems and Linux administration studies. The ability to manipulate file permissions using commands like chmod, chown, and chgrp is a practical skill that students must master. Whether you are configuring a web server, setting up development environments, or managing user access to shared resources, understanding file permissions is absolutely essential. This module will cover the theoretical foundations of file permissions and provide extensive practical examples to help you become proficient in managing access control in Linux systems.

## Key Concepts

### Understanding Permission Types

Linux file permissions are based on three distinct access types: read (r), write (w), and execute (x). Each of these permissions has specific meanings depending on whether they apply to files or directories.

For **regular files**, the permissions work as follows:

- **Read (r)**: Allows the user to view the contents of the file
- **Write (w)**: Allows the user to modify or delete the file
- **Execute (x)**: Allows the user to run the file as a program or script

For **directories**, the permissions have different interpretations:

- **Read (r)**: Allows listing of files within the directory
- **Write (w)**: Allows creating, deleting, or renaming files within the directory
- **Execute (x)**: Allows entering the directory and accessing its contents (traversal)

### Permission Categories

Linux permissions are assigned to three categories of users:

- **Owner (u)**: The user who owns the file
- **Group (g)**: Members of the file's group
- **Others (o)**: All other users on the system

This structure allows for granular control over who can access what. The combination of permission types and user categories creates a powerful access control system.

### Viewing Permissions with ls -l

The `ls -l` command displays detailed information about files, including their permissions. The output appears as a string of ten characters:

```
-rwxr-xr-- 1 user group 4096 Jan 15 10:30 filename
```

The first character indicates the file type:

- `-` : Regular file
- `d` : Directory
- `l` : Symbolic link
- `c` : Character device
- `b` : Block device
- `p` : Named pipe
- `s` : Socket

The remaining nine characters are divided into three groups of three:

- Positions 1-3: Owner permissions (rwx)
- Positions 4-6: Group permissions (r-x)
- Positions 7-9: Other permissions (r--)

### Numeric (Octal) Representation

Permissions can also be represented using octal numbers (base-8). Each permission type is assigned a numeric value:

- Read (r) = 4
- Write (w) = 2
- Execute (x) = 1

To calculate permissions for a category, you add the values together. For example:

- rwx = 4 + 2 + 1 = 7
- rw- = 4 + 2 + 0 = 6
- r-x = 4 + 0 + 1 = 5
- r-- = 4 + 0 + 0 = 4
- -w- = 0 + 2 + 0 = 2
- --x = 0 + 0 + 1 = 1

A complete permission set is represented by three digits. For example, 755 means:

- Owner: rwx (7)
- Group: r-x (5)
- Others: r-x (5)

This is the default permission for directories and executable files.

### Symbolic Representation

The symbolic method uses letters to modify permissions:

- `+` adds permissions
- `-` removes permissions
- `=` sets exact permissions

You can use abbreviations:

- u : owner
- g : group
- o : others
- a : all (owner + group + others)

Examples:

- `chmod u+x file` : Add execute permission for owner
- `chmod g-w file` : Remove write permission for group
- `chmod o=rw file` : Set exactly read and write for others
- `chmod a+x file` : Add execute permission for everyone

### The chmod Command

The `chmod` command is used to change file permissions. It supports both numeric and symbolic modes.

**Numeric mode examples:**

```bash
chmod 755 script.sh # rwxr-xr-x
chmod 644 document.txt # rw-r--r--
chmod 600 secret.key # rw-------
chmod 777 public.sh # rwxrwxrwx (risky!)
```

**Symbolic mode examples:**

```bash
chmod u+x file # Add execute for owner
chmod +x file # Add execute for all
chmod u=rwx,g=rx,o=r file # Explicit setting
chmod u-x,g-w file # Remove execute from owner, write from group
```

### Special Permissions

Beyond the basic rwx permissions, Linux supports three special permission bits:

**1. SUID (Set User ID) - 4xxx**
When set on an executable file, the program runs with the owner's privileges, regardless of which user runs it. Represented as 's' in the owner's execute position.

```bash
chmod 4755 program # -rwsr-xr-x
chmod u+s program
```

**2. SGID (Set Group ID) - 2xxx**
On executable files, it runs with the group's privileges. On directories, new files inherit the directory's group.

```bash
chmod 2755 directory # drwxr-sr-x
chmod g+s directory
```

**3. Sticky Bit - 1xxx**
On directories, only the owner can delete their own files. The /tmp directory uses this.

```bash
chmod 1777 /tmp # drwxrwxrwt
chmod +t directory
```

### Default Permissions and umask

When creating new files or directories, they are assigned default permissions. For files, this is typically 666 (rw-rw-rw-), and for directories, it's 777 (rwxrwxrwx). The `umask` value subtracts from these defaults.

If umask is 022:

- Files: 666 - 022 = 644 (rw-r--r--)
- Directories: 777 - 022 = 755 (rwxr-xr-x)

To check current umask:

```bash
umask
```

To set a new umask:

```bash
umask 027
```

## Examples

### Example 1: Setting Up a Web Directory

Suppose you have a web application in `/var/www/myapp` that needs to be readable by the web server but writable only by the owner.

**Step-by-step solution:**

1. Set directory permissions to 755 (owner full access, others read/execute):

```bash
chmod 755 /var/www/myapp
```

2. Set file permissions to 644 (owner read/write, others read):

```bash
chmod 644 /var/www/myapp/*.html
```

3. Make PHP files executable if needed:

```bash
chmod 644 /var/www/myapp/*.php
```

4. For directories within the app:

```bash
find /var/www/myapp -type d -exec chmod 755 {} \;
```

### Example 2: Creating a Shared Group Directory

You want to create a directory where multiple users in the "developers" group can collaborate.

**Step-by-step solution:**

1. Create the directory:

```bash
mkdir /project/shared
```

2. Set the group ownership:

```bash
chgrp developers /project/shared
```

3. Set SGID so new files inherit the group:

```bash
chmod 2775 /project/shared
```

4. Set permissions allowing group read/write/execute and others read:

```bash
# This gives: rwxrwsr-x
# Owner: rwx, Group: rwx with SGID, Others: r-x
```

5. Verify:

```bash
ls -ld /project/shared
# Output: drwxrwsr-x 2 owner developers 4096 Jan 15 10:30 /project/shared
```

### Example 3: Securing a Private Key File

You have an SSH private key that should only be accessible by your user account.

**Step-by-step solution:**

1. Check current permissions:

```bash
ls -l ~/.ssh/id_rsa
# May show: -rw-r--r-- 1 user user 1675 Jan 15 10:30 .ssh/id_rsa
```

2. Remove all permissions except owner read/write:

```bash
chmod 600 ~/.ssh/id_rsa
```

3. Verify:

```bash
ls -l ~/.ssh/id_rsa
# Output: -rw------- 1 user user 1675 Jan 15 10:30 .ssh/id_rsa
```

4. Also secure the .ssh directory:

```bash
chmod 700 ~/.ssh
```

### Example 4: Using Recursive Permissions

To change permissions for all files and subdirectories:

**For all files to 644:**

```bash
find /path/to/dir -type f -exec chmod 644 {} \;
```

**For all directories to 755:**

```bash
find /path/to/dir -type d -exec chmod 755 {} \;
```

**Combined approach (more efficient):**

```bash
find /path/to/dir -exec chmod {} \;
# Then separately fix directories:
find /path/to/dir -type d -exec chmod 755 {} \;
```

## Exam Tips

1. **Memorize the octal values**: Remember r=4, w=2, x=1. This is frequently tested in exams.

2. **Know common permission patterns**: 755 (standard for executables), 644 (standard for files), 600 (private files), 777 (world-writable - usually a security risk).

3. **Understand the difference between file and directory permissions**: This is a common exam question - know that execute on directories means "traverse".

4. **Special permissions are important**: Remember SUID (4), SGID (2), and Sticky Bit (1) for exams.

5. **Symbolic vs numeric mode**: Know both methods and when each is appropriate. Symbolic is better for modifying specific permissions.

6. **Default umask**: Remember that default file permissions are 666 and directories are 777, minus the umask value.

7. **Security considerations**: In exams, identify which permission settings are insecure (like 777) and suggest corrections.

8. **ls -l output interpretation**: Be able to read and interpret the ten-character permission string in both theoretical and practical questions.
