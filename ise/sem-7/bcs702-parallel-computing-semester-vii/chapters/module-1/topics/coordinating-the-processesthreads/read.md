c
    pthread_mutex_t lock; // Declare a mutex lock

    // Thread 1: Deposit
    pthread_mutex_lock(&lock); // Acquire Lock
    balance += amount;         // Critical Section
    pthread_mutex_unlock(&lock); // Release Lock

    // Thread 2: Withdraw
    pthread_mutex_lock(&lock); // Acquire Lock (will block if Thread 1 has it)
    balance -= amount;         // Critical Section
    pthread_mutex_unlock(&lock); // Release Lock