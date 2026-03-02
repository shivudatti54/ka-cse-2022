c
#include <pthread.h>
#include <stdio.h>

// The function that the thread will execute
void* print_message(void *msg) {
    char *message = (char *) msg;
    printf("%s\n", message);
    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;
    char *message1 = "Hello from Thread 1";
    char *message2 = "Hello from Thread 2";

    // Create two threads
    pthread_create(&thread1, NULL, print_message, (void*) message1);
    pthread_create(&thread2, NULL, print_message, (void*) message2);

    // Wait for both threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("Both threads have completed.\n");
    return 0;
}