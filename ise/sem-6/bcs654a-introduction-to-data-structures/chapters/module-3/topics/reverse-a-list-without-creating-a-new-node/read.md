cpp
// Function to reverse a linked list iteratively
Node* reverseLinkedList(Node* head) {
    Node *previous = NULL;
    Node *current = head;
    Node *next = NULL;

    while (current != NULL) {
        next = current->next;  // Store the next node
        current->next = previous; // Reverse the current node's pointer

        // Move pointers one position ahead
        previous = current;
        current = next;
    }
    head = previous; // previous is now the new head
    return head;
}