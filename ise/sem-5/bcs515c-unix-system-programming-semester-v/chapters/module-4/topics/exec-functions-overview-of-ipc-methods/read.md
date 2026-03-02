c
#include <unistd.h>
#include <stdio.h>

int main() {
pid_t pid = fork();

    if (pid == 0) { // Child process
        // Replace the child's image with the "ls" program
        execlp("ls", "ls", "-l", "/home", (char *)NULL);

        // If execlp returns, it means an error occurred
        perror("execlp failed");
        return 1;
    } else if (pid > 0) { // Parent process
        printf("Parent waiting for child (PID: %d)...\n", pid);
        wait(NULL); // Wait for the child to terminate
        printf("Child finished.\n");
    } else {
        perror("fork failed");
        return 1;
    }
    return 0;

}
