c
void producer() {
    while (true) {
        item = produce_item();   // Generate a new item
        wait(empty);            // Decrement empty count. Wait if buffer is full.
        wait(mutex);            // Acquire lock on the buffer
        add_item(item);         // Critical Section: Add item to the buffer
        signal(mutex);          // Release the lock
        signal(full);           // Increment full count. Signal a waiting consumer.
    }
}