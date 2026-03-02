c
void push(int stack[], int *top, int capacity, int value) {
    if (*top == capacity - 1) {
        printf("Stack Overflow! Cannot push %d.\n", value);
        return;
    }
    (*top)++;          // Move the top pointer up
    stack[*top] = value; // Place the value at the new top
    printf("%d pushed onto the stack.\n", value);
}