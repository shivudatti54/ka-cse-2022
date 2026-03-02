c
    // Example inspired by their style: Inserting at the front of a list
    struct Node {
        int data;
        struct Node* next;
    };

    void insertFront(struct Node** head_ref, int new_data) {
        struct Node* new_node = (struct Node*)malloc(sizeof(struct Node)); // 1. Allocate
        new_node->data = new_data;  // 2. Assign data
        new_node->next = *head_ref; // 3. Make new node point to current head
        *head_ref = new_node;       // 4. Move head to point to the new node
    }