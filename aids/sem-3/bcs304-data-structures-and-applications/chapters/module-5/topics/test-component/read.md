c
#include <stdio.h>
#include <stdlib.h>

// ... (Definitions for Node, List, insertAtEnd, deleteFromFront, displayList) ...

int main() {
    struct ListNode* head = NULL; // Start with an empty list

    // Test 1: Insertion and Display
    printf("Test 1: Inserting 10, 20, 30 at end:\n");
    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);
    displayList(head); // Output should be: 10 -> 20 -> 30 -> NULL

    // Test 2: Deletion from Front
    printf("\nTest 2: Deleting from front:\n");
    head = deleteFromFront(head);
    displayList(head); // Output should be: 20 -> 30 -> NULL

    // Test 3: Boundary Case - Delete until empty
    printf("\nTest 3: Deleting until list is empty:\n");
    head = deleteFromFront(head);
    displayList(head); // Output: 30 -> NULL
    head = deleteFromFront(head);
    displayList(head); // Output: List is Empty (NULL)

    // Test 4: Boundary Case - Delete from empty list
    printf("\nTest 4: Attempting to delete from an empty list:\n");
    head = deleteFromFront(head); // Should handle this gracefully without crashing

    return 0;
}