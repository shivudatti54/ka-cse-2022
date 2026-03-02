c
#include <stdio.h>

extern char **environ; // Declaration of the external global variable

int main() {
    for (int i = 0; environ[i] != NULL; i++) {
        printf("%s\n", environ[i]);
    }
    return 0;
}