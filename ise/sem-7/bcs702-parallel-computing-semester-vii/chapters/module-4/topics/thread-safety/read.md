c
#include <pthread.h>

int counter = 0;
pthread_mutex_t lock; // Declare a mutex

void* increment_counter(void* arg) {
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&lock);   // Acquire the lock before entering critical section
        counter++;                   // Critical Section
        pthread_mutex_unlock(&lock); // Release the lock
    }
    return NULL;
}

int main() {
    pthread_mutex_init(&lock, NULL); // Initialize the mutex
    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, increment_counter, NULL);
    pthread_create(&thread2, NULL, increment_counter, NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("Final counter value: %d\n", counter); // Will correctly be 200000
    pthread_mutex_destroy(&lock);
    return 0;
}