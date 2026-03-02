# Daemon Processes in Unix/Linux

## Introduction

A daemon process is a background-running process that operates independently of any user session and runs continuously in the background, typically waiting for certain events or conditions to occur before taking action. The term "daemon" originates from the Greek word "daimon," meaning a supernatural being performing tasks for others—quite apt for these tireless system servants. In Unix/Linux terminology, daemons are the backbone of system services, handling tasks ranging from network service management to log processing.

Daemon processes are essential for modern operating systems because they provide critical services without requiring user intervention or keeping terminals occupied. When you log out or close a terminal, daemons continue running, serving other processes and users. Examples include the Apache web server, SSH daemon, printing daemon (cupsd), and the cron scheduler. Understanding daemon processes is crucial for system administrators and software developers, as they frequently need to create daemon processes to implement background services in server applications.

## Key Concepts

### Characteristics of Daemon Processes

Daemon processes possess several distinguishing characteristics that set them apart from regular background processes. First, they are detached from any controlling terminal—they have no controlling terminal and are not associated with any terminal device. Second, they run with root privileges or specific user privileges to access system resources. Third, they typically have a parent process init (PID 1) or a process like systemd, which ensures they remain running even if their original parent terminates. Fourth, they operate in the background with no user interface, waiting silently for requests or conditions. Fifth, they are long-running processes that start at system boot and terminate only at system shutdown.

### Creating a Daemon Process

The process of creating a daemon involves several critical steps to ensure proper detachment from the controlling terminal. The standard procedure, often called "daemonizing," involves the following steps:

1. **Call fork() and terminate the parent process**: The first step creates a child process using fork(). After fork(), the parent process immediately exits. This is crucial because the shell thinks the command has completed, and the child now runs in the background.

2. **Call setsid() to create a new session**: The child process calls setsid() to become the leader of a new session and the leader of a new process group. This detaches the process from the controlling terminal, as the process no longer has a session leader.

3. **Fork again (optional but recommended)**: Many daemon implementations perform a second fork(). This prevents the daemon from acquiring a controlling terminal again, as the second child is not a session leader and cannot open a controlling terminal.

4. **Change the working directory**: The daemon should change its working directory to a safe location, typically the root directory (/). This prevents the daemon from preventing filesystem unmounts due to keeping directories open.

5. **Close standard file descriptors**: The daemon closes the standard input (stdin), standard output (stdout), and standard error (stderr) file descriptors. These are typically redirected to /dev/null or a log file to prevent any accidental output.

6. **Set file creation mask**: The umask is set to a known value (usually 0) to ensure the daemon can create files with appropriate permissions.

### Types of Daemon Processes

Daemon processes can be classified into two main categories based on how they are started and managed. **Standalone daemons** are independently started daemons that run continuously in memory, listening for service requests. Examples include httpd (Apache) and ftpd. These daemons are more memory-intensive but respond faster to requests since they're always running.

**Internet superservers** (inetd/xinetd) represent an alternative approach where a master daemon listens on multiple ports and spawns specific daemons only when needed. When a request arrives, the superserver forks a child process to handle that specific connection. This approach is memory-efficient but has slightly higher latency. The xinetd daemon is the modern replacement for the older inetd.

### Communication with Daemon Processes

Daemons often need to communicate with other processes or allow administrators to control them. Several mechanisms facilitate this communication. **PID files** are the simplest method—daemons write their Process ID to a file (typically in /var/run/) so other processes can send signals to them. **Unix domain sockets** provide local inter-process communication with good performance. Daemons can also use regular files in /var/ or /tmp/ directories to store status information. **Signals** like SIGHUP are commonly used to instruct daemons to reload configuration files without restarting.

### Common Daemons in Unix/Linux Systems

Several essential daemons run on typical Unix/Linux systems. The **cron daemon** executes scheduled commands at specific times. The **atd daemon** handles one-time scheduled tasks. The **syslogd** or **rsyslogd** daemon manages system log messages. The **sshd** daemon provides secure shell access. The **cupsd** daemon handles print services. The **ntpd** or **chronyd** daemon maintains system time synchronization. The **network manager** daemon handles network connections.

## Examples

### Example 1: Creating a Basic Daemon in C

Let's create a simple daemon process that writes the current time to a file every 10 seconds:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <time.h>
#include <fcntl.h>

void create_daemon() {
 pid_t pid;

 // Step 1: First fork
 pid = fork();
 if (pid < 0) {
 exit(EXIT_FAILURE);
 }
 if (pid > 0) {
 exit(EXIT_SUCCESS); // Parent exits
 }

 // Step 2: Become session leader
 if (setsid() < 0) {
 exit(EXIT_FAILURE);
 }

 // Step 3: Second fork (optional but recommended)
 pid = fork();
 if (pid < 0) {
 exit(EXIT_FAILURE);
 }
 if (pid > 0) {
 exit(EXIT_SUCCESS);
 }

 // Step 4: Change working directory to root
 chdir("/");

 // Step 5: Close standard file descriptors
 close(STDIN_FILENO);
 close(STDOUT_FILENO);
 close(STDERR_FILENO);

 // Step 6: Set file creation mask
 umask(0);
}

int main() {
 FILE *fp;
 time_t rawtime;
 struct tm *timeinfo;

 create_daemon();

 // Daemon work: write time to file every 10 seconds
 while (1) {
 fp = fopen("/tmp/daemon_time.txt", "a");
 if (fp != NULL) {
 time(&rawtime);
 timeinfo = localtime(&rawtime);
 fprintf(fp, "Current time: %s", asctime(timeinfo));
 fclose(fp);
 }
 sleep(10);
 }

 return 0;
}
```

### Example 2: Writing a Daemon PID File

After creating a daemon, it's good practice to write its PID to a file:

```c
void write_pid_file(const char *pid_file) {
 FILE *fp;

 fp = fopen(pid_file, "w");
 if (fp != NULL) {
 fprintf(fp, "%d\n", getpid());
 fclose(fp);
 }
}
```

### Example 3: Handling Signals in a Daemon

Daemons should handle signals gracefully, especially SIGHUP for configuration reload:

```c
#include <signal.h>

volatile sig_atomic_t reload_config = 0;

void sighup_handler(int signum) {
 reload_config = 1;
}

void setup_signal_handlers() {
 struct sigaction sa;
 sa.sa_handler = sighup_handler;
 sigemptyset(&sa.sa_mask);
 sa.sa_flags = SA_RESTART;
 sigaction(SIGHUP, &sa, NULL);
}
```

## Exam Tips

1. **Remember the six steps of daemon creation**: fork, setsid, fork again (optional), chdir to root, close standard file descriptors, and set umask to 0.

2. **Understand why two forks are recommended**: The second fork prevents the daemon from acquiring a controlling terminal, ensuring it remains truly detached.

3. **Know the difference between standalone and inetd/xinetd daemons**: Standalone daemons run continuously, while inetd-based daemons are spawned on demand.

4. **Remember common examples**: cron, atd, syslogd, sshd, httpd are frequently asked about in exams.

5. **Understand why daemons change working directory**: To prevent the filesystem from being locked and unable to unmount.

6. **Know the purpose of PID files**: They allow other processes (and administrators) to send signals to the daemon.

7. **Understand signal handling in daemons**: SIGHUP typically triggers configuration reload, while SIGTERM or SIGINT initiates graceful shutdown.
