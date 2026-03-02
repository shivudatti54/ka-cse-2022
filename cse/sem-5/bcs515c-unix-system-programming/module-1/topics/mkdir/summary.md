# mkdir - Making Directories in Linux/Unix - Summary

## Key Definitions and Concepts

- **mkdir**: A command-line utility in Unix-like systems used to create new directories (folders)
- **Directory**: A special file type that contains file names and metadata, organized in a hierarchical structure
- **Absolute Path**: A complete path starting from the root directory (e.g., `/home/student/projects`)
- **Relative Path**: A path relative to the current working directory (e.g., `./documents/reports`)
- **Parent Directory**: The directory that contains the current directory

## Important Formulas and Theorems

- **Basic Syntax**: `mkdir [OPTIONS] DIRECTORY_NAME`
- **Parent Directory Creation**: `mkdir -p /path/to/nested/dir` - Creates all intermediate directories
- **Permission Setting**: `mkdir -m 755 dirname` - Creates directory with specific octal permissions
- **Verbose Mode**: `mkdir -v dirname` - Displays messages for each created directory
- **Multiple Directories**: `mkdir dir1 dir2 dir3` - Creates multiple directories at once

## Key Points

- The `mkdir` command is part of GNU coreutils and available on all Unix-like systems
- Without `-p`, mkdir fails if parent directories don't exist
- Default directory permissions are 755 (rwxr-xr-x) for regular users
- The `-m` option accepts both octal (755) and symbolic (u=rwx,go=rx) modes
- Directory permissions include: read (list contents), write (create/delete files), execute (enter directory)
- mkdir returns exit status 0 for success and non-zero for failure
- Brace expansion `mkdir -p project/{src,docs,tests}` creates multiple directories efficiently
- The `.` and `..` entries are automatically created in every new directory

## Common Mistakes to Avoid

1. **Forgetting the -p flag** when creating nested directories, causing "No such file or directory" errors
2. **Incorrect path specification** - confusing absolute paths with relative paths
3. **Permission errors** - trying to create directories in locations without write access
4. **Not verifying** directory creation with `ls -ld` after running mkdir

## Revision Tips

1. Practice creating directory structures using both single commands and brace expansion
2. Remember that mkdir with `-p` is idempotent - running it multiple times is safe
3. Always check exit status when using mkdir in shell scripts
4. Understand the relationship between mkdir and system calls like mkdir() in programming
5. Review file permissions concepts alongside directory creation for complete understanding
