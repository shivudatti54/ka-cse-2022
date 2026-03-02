# Manipulating The Path - Summary

## Key Definitions
- **PATH**: An environment variable containing a colon-separated list of directories where the shell searches for executable commands
- **Environment Variable**: A named value that can affect the behavior of processes in Unix systems
- **Export**: A shell builtin that marks variables to be passed to child processes

## Important Formulas
- Prepend to PATH: `PATH=/new/directory:$PATH`
- Append to PATH: `PATH=$PATH:/new/directory`
- Display readable PATH: `echo $PATH | tr ':' '\n'`

## Key Points
- PATH directories are searched left-to-right; the first matching executable is used
- PATH modifications without export affect only the current shell, not child processes
- ~/.bashrc is the primary configuration file for interactive bash sessions
- Empty PATH entries (::) represent the current working directory
- Use which command to determine which executable will be executed
- PATH separators are colons (:) on Unix, semicolons (;) on Windows
- The current directory (.) should generally not be in PATH for security reasons

## Common Mistakes
- Forgetting to use export, causing PATH changes to not propagate to child processes
- Using semicolons instead of colons as PATH separators (common Windows confusion)
- Adding duplicate entries to PATH, which can cause confusion and slow command lookup
- Modifying /etc/profile without understanding system-wide implications
- Not verifying PATH changes immediately after making modifications