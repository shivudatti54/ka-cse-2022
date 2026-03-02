# Relative and Absolute Pathnames - Directory Commands - Summary

## Key Definitions and Concepts

- **Absolute Path**: Complete path starting from root (/), always begins with "/" - e.g., /home/student/documents/file.txt
- **Relative Path**: Path relative to current working directory, never begins with "/" - e.g., documents/file.txt
- **Root Directory (/)**: The topmost directory in Linux hierarchy from which all other directories branch
- **Current Working Directory**: The directory where the user is currently located (displayed by pwd command)
- **Home Directory (~)**: Default directory for a user, typically /home/username

## Important Commands

- **pwd**: Print Working Directory - displays current location in file system
- **cd [path]**: Change Directory - navigates to the specified path
- **ls [options] [path]**: Lists contents of directories (common options: -l, -a, -R)
- **mkdir [options] [path]**: Creates new directories (-p for nested creation)
- **rmdir [path]**: Removes empty directories

## Special Directory References

- **.** (dot): Current directory
- **..** (double dot): Parent directory (one level up)
- **~** (tilde): Current user's home directory
- **-** (hyphen): Previous working directory (used only with cd command)

## Key Points

1. Absolute paths always start from root (/) and work correctly from any location in the file system
2. Relative paths depend entirely on the current working directory context
3. The Linux file system is hierarchical with "/" as the single root point
4. Always use pwd to verify current location before using relative paths
5. mkdir -p creates nested directories and doesn't fail if directories already exist
6. cd - toggles conveniently between current and previous directory
7. Hidden files in Linux start with "." and require ls -a to display them
8. Understanding path resolution is crucial for scripting and automation
9. The home directory (~) provides a reliable shortcut regardless of current location

## Common Mistakes to Avoid

1. Forgetting the leading "/" in absolute paths - this makes a path relative
2. Using relative paths without first checking current directory with pwd
3. Confusing "." (current directory) with ".." (parent directory)
4. Attempting rmdir on non-empty directories (use rm -r instead)
5. Using spaces in directory names without proper quoting

## Revision Tips

1. Practice navigating using both absolute and relative paths in a Linux terminal
2. Memorize the tree-like structure of Linux directories (/bin, /etc, /home, /var, etc.)
3. Use cd - frequently to quickly switch between two commonly-used directories
4. Always run pwd before using relative paths in shell scripts
5. Remember that ~ is equivalent to /home/username for regular users
6. Get comfortable with the -p flag in mkdir for creating complex directory structures
