c
// Definition of the TestAndSet function
bool TestAndSet(bool *lock) {
    bool original_value = *lock; // 1. Read the current value of the lock
    *lock = true;               // 2. Set the lock to TRUE (locked), unconditionally
    return original_value;      // 3. Return the original value that was read
}