# Daemon Processes - Summary

## Key Definitions and Concepts

A **daemon process** is a background-running process that operates independently of user sessions, typically providing system services. It runs continuously from system startup to shutdown, detached from any controlling terminal.

## Important Formulas and Theorems

The daemon creation process follows this sequence:

- `fork()` → Parent exits, child continues
- `setsid()` → Create new session, detach from terminal
- Second `fork()` (optional) → Prevent controlling terminal acquisition
- `chdir("/")` → Change to root directory
- `close(STDIN, STDOUT, STDERR)` → Close standard file descriptors
- `umask(0)` → Set file creation mask

## Key Points

- Daemon processes have no controlling terminal and run in the background
- The init process (PID 1) or systemd becomes the parent of orphaned daemons
- Two forks are recommended to fully detach from controlling terminals
- Daemons typically change working directory to root to prevent mount issues
- Standard file descriptors are closed or redirected to /dev/null or log files
- Standalone daemons run continuously; inetd/xinetd spawns daemons on demand
- PID files in /var/run/ allow other processes to communicate with daemons
- SIGHUP is commonly used to trigger configuration reload in daemons

## Common Mistakes to Avoid

- Forgetting to exit the parent after fork(), which leaves a zombie-like process
- Not calling setsid() before the second fork, which can cause terminal-related issues
- Failing to close file descriptors, which can prevent filesystem unmounting
- Not handling signals, which can make daemons difficult to manage

## Revision Tips

- Practice writing the daemon creation code from memory
- Remember the acronym: F-S-F-C-C-U (Fork, Session leader, Fork, Chdir, Close, Umask)
- Compare standalone vs inetd/xinetd daemons with a table
- Review common system daemons and their purposes
