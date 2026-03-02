# Daemon Characteristics - Summary

## Key Definitions and Concepts

- **Daemon**: A background process that runs continuously, detached from any controlling terminal, providing system services from boot until shutdown
- **Controlling Terminal**: The terminal from which a process is started; daemons must detach from this
- **Double-Fork Technique**: The method of calling fork() twice to ensure a daemon cannot acquire a controlling terminal
- **Orphan Process**: A process whose parent has terminated; daemons become orphans intentionally and are adopted by init (PID 1)

## Important Formulas and Theorems

The daemon creation process follows these six essential steps:

1. **fork()** - Create child process, parent exits
2. **setsid()** - Create new session, become session leader
3. **fork() (optional)** - Second fork to prevent terminal acquisition
4. **chdir("/")** - Change working directory to root
5. **umask(0)** - Set file creation mask to zero
6. **close(STDIN, STDOUT, STDERR)** - Close or redirect standard file descriptors

## Key Points

- Daemons run without user interaction and provide background services
- They have no controlling terminal - this is the defining characteristic
- Their parent process is always init/systemd (PID 1)
- Daemons change working directory to prevent blocking file system unmounts
- Standard file descriptors are closed and redirected to /dev/null or log files
- Common daemons include: cron (scheduling), syslogd (logging), httpd (web), sshd (remote access), cupsd (printing)
- Daemons handle signals: SIGHUP (reload), SIGTERM (graceful exit), SIGKILL (forced exit)
- Modern Linux uses systemd to manage daemons as services with dependencies

## Common Mistakes to Avoid

- Confusing a background process (started with &) with a daemon - background processes still have a controlling terminal
- Forgetting to close all three standard file descriptors (stdin, stdout, stderr)
- Not changing the working directory, which can prevent file systems from being unmounted
- Skipping the second fork in implementations where preventing terminal acquisition is necessary
- Setting umask incorrectly, which can lead to permission issues with files created by the daemon

## Revision Tips

1. Memorize the six-step daemon creation sequence in order
2. For each step, remember WHY it's necessary (e.g., chdir prevents blocking unmounts)
3. Practice tracing through example C code to understand daemon creation flow
4. Remember the file descriptor numbers: stdin=0, stdout=1, stderr=2
5. Review signal handling: know that SIGHUP typically triggers config reload
6. Be able to list at least 5 common daemons and their purposes
