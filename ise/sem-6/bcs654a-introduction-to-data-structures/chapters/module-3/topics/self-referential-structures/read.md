c
struct node {
    int data;           // Data part (can be any data type)
    struct node *next;  // Pointer to another node (the self-reference)
};