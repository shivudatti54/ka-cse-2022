c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to reverse the linked list iteratively
void reverse(struct Node** head_ref) {
    struct Node* prev = NULL;
    struct Node* curr = *head_ref;
    struct Node* next = NULL;

    while (curr != NULL) {
        next = curr->next; // Store next node
        curr->next = prev; // Reverse current node's pointer
        prev = curr;       // Move prev to current
        curr = next;       // Move current to next
    }
    *head_ref = prev; // Update head to new first node
}