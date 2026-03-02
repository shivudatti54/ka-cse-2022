c
#include <pthread.h>
#include <stdio.h>

void* thread_function(void* arg) {
    int thread_id = *((int*)arg);
    printf("Hello from thread %d\n", thread_id);
    pthread_exit(NULL);
}

int main() {
    pthread_t thread_id;
    int id_value = 123;

    // Create a new thread
    if(pthread_create(&thread_id, NULL, thread_function, &id_value)) {
        fprintf(stderr, "Error creating thread\n");
        return 1;
    }

    // Wait for the created thread to finish
    pthread_join(thread_id, NULL);

    printf("Main thread exiting.\n");
    return 0;
}