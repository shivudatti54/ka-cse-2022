c
// Function to insert a new node at the beginning
void insertAtBeginning(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node)); // 1. Allocate
    new_node->data = new_data;                                       // 2. Put data
    new_node->next = (*head_ref);                                    // 3. Make next of new node as head
    (*head_ref) = new_node;                                          // 4. Move head to point to the new node
}