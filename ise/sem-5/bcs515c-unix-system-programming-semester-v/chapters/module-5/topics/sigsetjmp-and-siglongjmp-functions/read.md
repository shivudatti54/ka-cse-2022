c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <setjmp.h>
#include <signal.h>

static sigjmp_buf jmpbuf; /_ Global jump buffer _/

/_ Signal Handler for SIGINT _/
void sigint_handler(int signo) {
printf("\nSIGINT received!\n");
/_ Perform cleanup here if needed (e.g., closing files) _/
siglongjmp(jmpbuf, 1); /_ Jump back to main, returning 1 _/
}

int main() {
struct sigaction act;

    /* Set up the signal handler for SIGINT */
    act.sa_handler = sigint_handler;
    sigemptyset(&act.sa_mask);
    act.sa_flags = 0;

    if (sigaction(SIGINT, &act, NULL) < 0) {
        perror("sigaction error");
        exit(EXIT_FAILURE);
    }

    /* Set the jump point. Save the signal mask (savemask=1). */
    if (sigsetjmp(jmpbuf, 1) == 0) {
        printf("Jump point set. Waiting for SIGINT (Ctrl+C)...\n");
    } else {
        printf("Returned from siglongjmp inside the handler.\n");
        /* After the jump, the signal mask is restored to its original state. */
    }

    /* Infinite loop to keep the program alive */
    while(1) {
        pause(); /* Wait for any signal */
    }

    return 0;

}
