c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid;
    pid = fork(); // Create a new process

    if (pid < 0) {
        fprintf(stderr, "Fork failed");
        return 1;
    } else if (pid == 0) {
        // This block is executed by the CHILD process
        printf("Hello from the Child! My PID is %d\n", getpid());
    } else {
        // This block is executed by the PARENT process
        printf("Hello from the Parent! My child's PID is %d\n", pid);
    }
    return 0;
}