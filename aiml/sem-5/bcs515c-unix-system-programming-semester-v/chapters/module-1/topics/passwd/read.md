c
#include <stdio.h>
#include <sys/types.h>
#include <pwd.h>

int main() {
    struct passwd *pwd;
    uid_t uid = 1000; // Example UID

    pwd = getpwuid(uid);
    if (pwd == NULL) {
        perror("getpwuid");
        return 1;
    }

    printf("User Name: %s\n", pwd->pw_name);
    printf("User ID: %d\n", pwd->pw_uid);
    printf("Home Dir: %s\n", pwd->pw_dir);

    return 0;
}