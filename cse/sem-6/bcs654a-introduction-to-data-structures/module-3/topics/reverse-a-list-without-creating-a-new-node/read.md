c
// Function to reverse a linked list iteratively
void reverseList(struct Node\*_ head_ref) {
struct Node_ previous = NULL;
struct Node* current = *head_ref;
struct Node\* next_node = NULL;

while (current != NULL) {
// Store the next node
next_node = current->next;

// Reverse current node's pointer
current->next = previous;

// Move pointers one position ahead
previous = current;
current = next_node;
}
// Update the head to point to the new front
\*head_ref = previous;

}
