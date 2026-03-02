c
#include <signal.h>

int sigaction(int signum, const struct sigaction *restrict act,
              struct sigaction *restrict oldact);