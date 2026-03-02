c
#include <stdio.h>
#include <unistd.h> // for vfork, exec
#include <sys/wait.h> // for wait

int main() {
int pid;
int parent_var = 100;

    printf("Parent: Before vfork(), parent_var = %d\n", parent_var);

    pid = vfork(); // Create child using vfork

    if (pid == 0) {
        // This is the CHILD process
        printf("Child: Started. parent_var = %d\n", parent_var);
        parent_var = 200; // !! DANGEROUS: Modifying parent's variable !!
        printf("Child: Modified parent_var to %d\n", parent_var);

        // CORRECT & SAFE: Immediately call exec()
        execl("/bin/date", "date", (char *)NULL);

        // If exec fails, we MUST call _exit(), not return or exit().
        perror("execl failed");
        _exit(1);
    }
    else if (pid > 0) {
        // This is the PARENT process (resumes after child execs/exits)
        printf("Parent: Resumed after child. parent_var = %d\n", parent_var);
        wait(NULL); // Wait for child to exit
    }
    else {
        // vfork failed
        perror("vfork failed");
        return 1;
    }
    return 0;

}
