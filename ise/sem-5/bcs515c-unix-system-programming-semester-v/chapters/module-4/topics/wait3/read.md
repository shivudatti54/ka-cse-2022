c
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/resource.h>

pid_t wait3(int *stat_loc, int options, struct rusage *rusage);
