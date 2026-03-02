c
// C Example of Static Allocation (Array)
#define MAX_SIZE 100
int arr[MAX_SIZE]; // Fixed-size array allocated at compile time
int top = -1; // For stack implementation

void push(int data) {
    if (top == MAX_SIZE - 1) {
        printf("Stack Overflow!"); // Fixed size limit reached
        return;
    }
    arr[++top] = data; // Simple, O(1) operation
}