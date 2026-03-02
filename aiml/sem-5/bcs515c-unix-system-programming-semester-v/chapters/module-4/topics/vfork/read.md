c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    int parent_var = 100; // A variable in the parent's space

    printf("Parent (PID: %d) before vfork(). parent_var = %d\n", getpid(), parent_var);

    // Create a new process using vfork
    pid = vfork();

    if (pid < 0) {
        // Error handling
        perror("vfork failed");
        return 1;
    } else if (pid == 0) {
        // This is the CHILD process
        printf("Child process (PID: %d) started. parent_var = %d\n", getpid(), parent_var);

        // Child can access parent's variables (DANGEROUS in general)
        parent_var = 200; // Modifying the parent's variable!
        printf("Child modified parent_var to: %d\n", parent_var);

        // CORRECT: The child must now call exec() or _exit()
        // Let's exec the 'ls' command
        execl("/bin/ls", "ls", "-l", (char *)NULL);

        // If execl fails, we MUST call _exit(), not exit() or return.
        perror("execl failed");
        _exit(1); // Use _exit() to avoid flushing stdio buffers shared with parent.

    } else {
        // This is the PARENT process
        // Execution resumes only after the child has exited or exec'd.
        printf("Parent (PID: %d) resumed. parent_var is now: %d\n", getpid(), parent_var);
    }

    return 0;
}