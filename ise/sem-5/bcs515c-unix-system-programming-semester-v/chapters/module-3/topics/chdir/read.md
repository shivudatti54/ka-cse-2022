c
#include <stdio.h>
#include <unistd.h> // for chdir, getcwd
#include <stdlib.h> // for exit

int main() {
char cwd[1024]; // Buffer to hold the current working directory

    // Get and print the current working directory
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("Current working dir: %s\n", cwd);
    } else {
        perror("getcwd() error");
        exit(1);
    }

    // Change directory to /tmp
    if (chdir("/tmp") == 0) {
        printf("Changed to /tmp successfully.\n");
    } else {
        perror("chdir() error");
        exit(1);
    }

    // Get and print the new current working directory
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("New current working dir: %s\n", cwd);
    } else {
        perror("getcwd() error after chdir");
        exit(1);
    }

    return 0;

}
