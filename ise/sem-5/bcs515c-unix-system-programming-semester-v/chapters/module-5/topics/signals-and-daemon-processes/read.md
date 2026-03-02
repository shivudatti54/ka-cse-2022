c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void sigint_handler(int sig) {
write(STDOUT_FILENO, "\nCaught SIGINT! (But not exiting)\n", 33);
}

int main() {
struct sigaction sa;
sa.sa_handler = sigint_handler;
sigemptyset(&sa.sa_mask);
sa.sa_flags = 0;

    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    while(1) {
        printf("Sleeping...\n");
        sleep(1);
    }
    return 0;

}
