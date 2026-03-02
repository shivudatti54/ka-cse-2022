c
#include <stdio.h>
#include <unistd.h>

int main() {
pid_t pid; // pid_t is the data type for process IDs

    pid = fork(); // Create a new process

    if (pid < 0) {
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (pid == 0) {
        // This block is executed only by the child process
        printf("Hello from the Child! My PID is %d\n", getpid());
    } else {
        // This block is executed only by the parent process
        printf("Hello from the Parent! My PID is %d, my Child's PID is %d\n", getpid(), pid);
    }
    return 0;

}
