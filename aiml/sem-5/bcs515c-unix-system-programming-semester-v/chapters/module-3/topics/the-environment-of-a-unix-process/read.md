c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // Print the process ID and parent process ID
    printf("PID: %d, PPID: %d\n", getpid(), getppid());
    
    // Print the current working directory
    char cwd[256];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("CWD: %s\n", cwd);
    } else {
        perror("getcwd");
    }
    
    // Set and print an environment variable
    setenv("MY_VAR", "example", 1);
    printf("MY_VAR: %s\n", getenv("MY_VAR"));
    
    return 0;
}