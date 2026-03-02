c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

void sigchld_handler(int signo) {
int status;
pid_t pid;

    // Use waitpid with WNOHANG in a loop to reap ALL terminated children.
    while ((pid = waitpid(-1, &status, WNOHANG)) > 0) {
        if (WIFEXITED(status)) {
            printf("Child process %d exited with status %d\n", pid, WEXITSTATUS(status));
        }
        // Handle other cases (e.g., signaled) if needed.
    }

}

int main() {
pid_t child_pid;

    // Establish the signal handler *before* creating the child.
    struct sigaction sa;
    sa.sa_handler = sigchld_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART | SA_NOCLDSTOP; // SA_NOCLDSTOP is optional for termination only.

    if (sigaction(SIGCHLD, &sa, NULL) == -1) {
        perror("sigaction");
        exit(1);
    }

    // Create a child process
    if ((child_pid = fork()) == 0) {
        /* Child process */
        printf("Child (PID: %d) is running...\n", getpid());
        sleep(2); // Simulate some work
        printf("Child exiting now.\n");
        exit(42); // Child exits with a status of 42
    } else if (child_pid > 0) {
        /* Parent process */
        printf("Parent (PID: %d) created child %d. Waiting for SIGCHLD...\n", getpid(), child_pid);
        // The parent can do its own work here. It doesn't need to block on wait().
        while(1) {
            printf("Parent is working...\n");
            sleep(1);
        }
    } else {
        perror("fork");
        exit(1);
    }
    return 0;

}
