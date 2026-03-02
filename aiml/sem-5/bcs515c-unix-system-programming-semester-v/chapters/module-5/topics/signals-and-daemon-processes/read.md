c
    #include <signal.h>
    void (*signal(int signum, void (*handler)(int)))(int);