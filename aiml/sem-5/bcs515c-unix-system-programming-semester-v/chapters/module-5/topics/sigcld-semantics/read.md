c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void sigchld_handler(int signo) {
    int status, pid;
    // Reap all available zombie children without blocking
    while ((pid = waitpid(-1, &status, WNOHANG)) > 0) {
        printf("Child PID %d terminated with status %d\n", pid, status);
    }
}

int main() {
    struct sigaction sa;

    // Set up the sigaction structure
    sa.sa_handler = sigchld_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART | SA_NOCLDSTOP; // SA_NOCLDSTOP is optional for termination only

    // Establish the handler using sigaction()
    if (sigaction(SIGCHLD, &sa, NULL) == -1) {
        perror("sigaction");
        exit(1);
    }

    // Fork a child process
    if (fork() == 0) {
        // Child code
        printf("Child PID %d starting...\n", getpid());
        sleep(2); // Simulate some work
        exit(42); // Child exits
    }

    // Parent code
    printf("Parent PID %d waiting...\n", getpid());
    while(1) {
        pause(); // Parent sleeps until a signal is received
    }
    return 0;
}