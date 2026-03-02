# **Files and Dictionaries: mkdir and rmdir functions**

## **Introduction**

In UNIX system programming, files and directories play a crucial role in organizing and managing data. Two essential functions that help create and delete files and directories are `mkdir` (make directory) and `rmdir` (remove directory). In this section, we will explore the definitions, explanations, and examples of these two functions.

## **Mkdir Function**

### Definition

The `mkdir` function is used to create a new directory in the file system.

### Explanation

The `mkdir` function is a built-in function in UNIX that creates a new directory with the specified name. The directory is created in the current working directory by default. If the directory already exists, the function returns an error.

### Syntax

```bash
mkdir [options] dirname
```

### Options

- `-p`: If the directory does not exist, create it.
- `-v`: Verbose mode, prints each command before executing it.

### Examples

- Create a new directory called `mydir`:

```bash
mkdir mydir
```

- Create a new directory called `mydir` with verbose mode:

```bash
mkdir -v mydir
```

- Create a new directory called `mydir` if it does not exist:

```bash
mkdir -p mydir
```

## **Rmdir Function**

### Definition

The `rmdir` function is used to remove an existing directory in the file system.

### Explanation

The `rmdir` function is a built-in function in UNIX that removes an existing directory with the specified name. The directory is removed only if it is empty. If the directory is not empty, the function returns an error.

### Syntax

```bash
rmdir [options] dirname
```

### Options

- `-i`: If the directory is not empty, prompt the user before removing it.
- `-p`: Do not remove the directory if it is not empty.

### Examples

- Remove an empty directory called `mydir`:

```bash
rmdir mydir
```

- Remove a non-empty directory called `mydir` and prompt the user:

```bash
rmdir -i mydir
```

- Remove a non-empty directory called `mydir` and do not remove if it is not empty:

```bash
rmdir -p mydir
```

### Key Concepts

- **Directory**: A collection of files and subdirectories.
- **Subdirectory**: A directory contained within another directory.
- **Empty directory**: A directory that has no files or subdirectories.
- **Non-empty directory**: A directory that has files or subdirectories.
- **Current working directory**: The directory from which commands are executed.

## **Conclusion**

In this section, we have learned about the `mkdir` and `rmdir` functions in UNIX system programming. These functions are essential for creating and deleting files and directories, and understanding their usage is crucial for effective UNIX system programming.
