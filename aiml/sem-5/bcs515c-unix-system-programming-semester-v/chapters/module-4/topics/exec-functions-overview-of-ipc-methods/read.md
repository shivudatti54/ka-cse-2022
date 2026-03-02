c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // This is the child process
        printf("Child PID: %d\n", getpid());
        // Replace the child's memory space with the "ls" program
        execlp("ls", "ls", "-l", NULL); // argv[0]="ls", argv[1]="-l"

        // If execlp returns, it means an error occurred
        perror("execlp failed");
        return 1;
    } else if (pid > 0) {
        // This is the parent process
        wait(NULL); // Wait for the child to terminate
        printf("Child finished.\n");
    } else {
        perror("fork failed");
        return 1;
    }
    return 0;
}