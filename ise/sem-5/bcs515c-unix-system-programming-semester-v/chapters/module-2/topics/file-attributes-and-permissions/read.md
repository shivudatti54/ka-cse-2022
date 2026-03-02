# File Attributes and Permissions

## 1. Introduction to File Attributes

In a Unix/Linux system, every file and directory has a set of metadata associated with it, known as **file attributes**. These attributes are not part of the file's content but describe its characteristics, such as who owns it, when it was last modified, its size, and, most importantly, its access permissions.

Understanding these attributes is fundamental to system security and administration, as they control how users and processes interact with files and directories.

## 2. Viewing File Attributes with `ls`

The primary command for viewing file attributes is `ls` (list). While a simple `ls` shows only filenames, its various options reveal detailed attribute information.

### The `-l` (Long Listing) Option

The most important option is `ls -l`, which provides a detailed, columnar view of file attributes.

```bash
$ ls -l
total 24
drwxr-xr-x 2 alice users 4096 Mar 10 14:30 Documents
-rw-r--r-- 1 alice users  220 Mar  9 11:22 hello.txt
-rwxr-xr-x 1 alice users 8464 Mar  8 10:15 my_script.sh
```

Let's break down the output of `ls -l`:

| Position | Example        | Meaning                                                                                              |
| :------- | :------------- | :--------------------------------------------------------------------------------------------------- |
| 1        | `drwxr-xr-x`   | **File type and permissions** (explained in detail in the next section).                             |
| 2        | `2`            | **Link count**: Number of hard links to the file/directory.                                          |
| 3        | `alice`        | **Owner (User)**: The username of the user who owns the file.                                        |
| 4        | `users`        | **Group**: The group that owns the file.                                                             |
| 5        | `4096`         | **Size**: Size of the file in bytes. For directories, this is often 4096 (the size of the metadata). |
| 6        | `Mar 10 14:30` | **Last modified timestamp**: The date and time the file was last modified.                           |
| 7        | `Documents`    | **Filename**.                                                                                        |

### Other Useful `ls` Options

- `ls -a`: Lists all files, including **hidden files** (those whose names begin with a dot `.`).
- `ls -lh`: The `-h` option shows file sizes in a **human-readable** format (e.g., K, M, G) instead of bytes.
- `ls -ld`: When used with a directory name (e.g., `ls -ld /tmp`), it shows information about the **directory itself**, not its contents.
- `ls -li`: The `-i` option shows the **inode number**, a unique identifier for the file on the filesystem.

## 3. Understanding File Permissions

The first field of the `ls -l` output is the most critical for security. It is a 10-character string that defines the **file type** and **permissions**.

### The Permission String Breakdown

The 10 characters can be broken into four groups: `[File Type][User Permissions][Group Permissions][Other Permissions]`.

```
    d    r w x    r - x    r - x
    |     | | |    | | |    | | |
    |     | | |    | | |    | | +-- Execute permission for Others
    |     | | |    | | |    | +---- Write permission for Others
    |     | | |    | | |    +------ Read permission for Others
    |     | | |    | | |
    |     | | |    | | +----------- Execute permission for Group
    |     | | |    | +------------- Write permission for Group
    |     | | |    +--------------- Read permission for Group
    |     | | |
    |     | | +-------------------- Execute permission for User (Owner)
    |     | +---------------------- Write permission for User (Owner)
    |     +------------------------ Read permission for User (Owner)
    |
    +------------------------------ File Type (-, d, l, etc.)
```

#### File Type

The first character indicates the file type:

| Symbol | File Type                              |
| :----- | :------------------------------------- |
| `-`    | Regular file (e.g., text file, binary) |
| `d`    | Directory                              |
| `l`    | Symbolic link                          |
| `c`    | Character special device               |
| `b`    | Block special device                   |
| `p`    | Named pipe (FIFO)                      |
| `s`    | Socket                                 |

#### Permission Classes

Permissions are defined for three classes of users:

1.  **User (u)**: The owner of the file.
2.  **Group (g)**: Users who are members of the file's group.
3.  **Others (o)**: All other users on the system.

#### Permission Types

For each class, three types of permissions can be granted:

| Symbol | Permission | Effect on a File                                           | Effect on a Directory                                                                                    |
| :----- | :--------- | :--------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| `r`    | Read       | Allows the file to be opened and read.                     | Allows listing of directory contents (e.g., with `ls`).                                                  |
| `w`    | Write      | Allows the file to be modified, truncated, or overwritten. | Allows creating, deleting, or renaming files **within** the directory (requires execute permission too). |
| `x`    | Execute    | Allows the file to be executed as a program or script.     | Allows accessing (entering) the directory and accessing files/subdirectories inside it (the **key**).    |
| `-`    | None       | The permission is not granted.                             | The permission is not granted.                                                                           |

**Crucial Note on Directory `w` and `x`:** To delete a file inside a directory, you need **write permission on the directory**, not on the file itself. The `x` permission (often called the "search" bit) is required to access any file or subdirectory within it. Without `x` on a directory, you cannot `cd` into it or access any of its contents, even if you have full permissions on the files inside.

## 4. Changing File Permissions with `chmod`

The `chmod` (change mode) command is used to alter file permissions. There are two ways to use it: **Symbolic Mode** and **Absolute (Octal) Mode**.

### Symbolic Mode

This method uses letters and symbols to add (`+`), remove (`-`), or set (`=`) permissions for specific classes.

**Format:** `chmod [who][operator][permissions] file_name`

- **Who:** `u` (user), `g` (group), `o` (others), `a` (all, equivalent to `ugo`)
- **Operator:** `+` (add), `-` (remove), `=` (set exactly)
- **Permissions:** `r` (read), `w` (write), `x` (execute)

**Examples:**

```bash
$ chmod o+w report.txt     # Add write permission for others on report.txt
$ chmod g-x script.sh      # Remove execute permission from the group on script.sh
$ chmod a=rw config.cfg    # Set permissions for everyone to read and write (no execute)
$ chmod ugo+r,.log         # Add read permission for all classes on all .log files
```

### Absolute (Octal) Mode

This method uses a 3-digit octal number (base-8) to represent permissions for all three classes (User, Group, Others) simultaneously. Each digit is the sum of the values for the permissions you want to grant.

| Permission  | Value |
| :---------- | :---- |
| Read (r)    | 4     |
| Write (w)   | 2     |
| Execute (x) | 1     |
| None (-)    | 0     |

To calculate the digit for a class, add the values of the permissions you want.

**Examples:**

- `rwx` = 4+2+1 = **7**
- `rw-` = 4+2+0 = **6**
- `r-x` = 4+0+1 = **5**
- `r--` = 4+0+0 = **4**
- `---` = 0+0+0 = \*\*0`

**Format:** `chmod nnn file_name` (where `nnn` is a 3-digit number)

**Examples:**

```bash
$ chmod 755 my_script.sh   # rwx for user, r-x for group and others (rwxr-xr-x)
$ chmod 644 index.html     # rw- for user, r-- for group and others (rw-r--r--)
$ chmod 600 secret.txt     # rw- for user, --- for group and others (rw-------)
```

## 5. Special Permissions: Setuid, Setgid, and Sticky Bit

Beyond the basic permissions, there are three special permission bits.

### Set User ID (Setuid) - `s` / `S`

- **Symbol:** `s` in the user execute field (e.g., `-rwsr-xr-x`)
- **Octal:** Prepend `4` to the mode (e.g., `4755`)
- **Effect:** When an executable file with setuid is run, it executes with the **privileges of the file's owner** (usually root), not the user who launched it. This is used for commands like `passwd` that need elevated privileges to modify system files like `/etc/shadow`.

### Set Group ID (Setgid) - `s` / `S`

- **On a File:** Behaves like setuid, but runs with the **privileges of the file's group**.
- **On a Directory:** `s` in the group execute field (e.g., `drwxrwsr-x`). **Files created inside this directory will automatically inherit the directory's group ownership**, not the primary group of the user who created them. This is crucial for collaborative directories.
- **Octal:** Prepend `2` to the mode (e.g., `2775` for a directory).

### Sticky Bit - `t` / `T`

- **Symbol:** `t` in the others execute field (e.g., `drwxrwxrwt`).
- **Octal:** Prepend `1` to the mode (e.g., `1777`).
- **Effect:** **Only the file's owner (or root) can delete or rename a file** within a directory that has the sticky bit set, even if others have write permission on the directory. The classic example is the `/tmp` directory, where all users can create files, but cannot delete each other's files.

## 6. Changing Ownership with `chown` and `chgrp`

Permissions are tied to ownership. You can change the owner and group of a file.

- `chown` (change owner): `chown new_owner filename`
- `chown` can also change the group: `chown new_owner:new_group filename`
- `chgrp` (change group): `chgrp new_group filename`

**Note:** Typically, only the root user can change the ownership of a file.

**Example:**

```bash
# Make root the owner of the file
$ sudo chown root my_app

# Change the group to 'www-data'
$ sudo chgrp www-data index.html

# Change both owner and group in one command
$ sudo chown alice:developers source_code.c
```

## 7. Default Permissions and `umask`

When a new file or directory is created, it receives a set of **default permissions**. These are not arbitrary; they are calculated by subtracting the value of the **umask** from a base permission set.

- **Base permission for a directory:** `777` (rwxrwxrwx)
- **Base permission for a file:** `666` (rw-rw-rw-) (No execute by default for safety)

The `umask` is a 3-digit octal value that specifies which permissions should be **masked out** (disallowed) by default.

**View your current umask:**

```bash
$ umask
0022
```

**Set a new umask (often in shell startup files like ~/.bashrc):**

```bash
$ umask 002
```

**Calculation Example (umask = 022):**

- **New Directory:** `777 - 022 = 755` -> `drwxr-xr-x`
- **New File:** `666 - 022 = 644` -> `-rw-r--r--`

**Calculation Example (umask = 002):**

- **New Directory:** `777 - 002 = 775` -> `drwxrwxr-x` (group can write)
- **New File:** `666 - 002 = 664` -> `-rw-rw-r--` (group can write)

## Exam Tips

1.  **Memorize the `ls -l` output format.** Be able to identify the owner, group, size, and permissions from a given line.
2.  **Understand the difference between file and directory permissions.** Remember that directory `x` (execute) means "access," and directory `w` means you can alter the directory's contents (create/delete files).
3.  **Practice both `chmod` syntaxes.** You should be fluent in both symbolic (`u+x`) and absolute (`755`) modes. Exams often ask to "set permissions to rwxr-x---" – know how to do that both ways.
4.  **Know the octal values.** Be able to quickly calculate that `rwx` is 7, `r-x` is 5, etc. This is a very common question.
5.  **Understand the special bits.** Know what setuid, setgid (on directories), and the sticky bit do and what their octal values are (4, 2, 1).
6.  **Understand `umask` calculation.** Don't just memorize that umask 022 gives 644/755. Understand that it's a subtractive mask from a base value.
