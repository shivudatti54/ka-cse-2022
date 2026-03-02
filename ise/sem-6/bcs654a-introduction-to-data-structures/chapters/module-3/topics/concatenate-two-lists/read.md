cpp
#include <iostream>
using namespace std;

// Definition of a Node
class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Function to concatenate two lists
// list1: The first list (will be modified to point to list2)
// list2: The second list
void concatenate(Node*& head1, Node* head2) {
    // If the first list is empty, it becomes the second list
    if (head1 == nullptr) {
        head1 = head2;
        return;
    }

    // Traverse to the last node of the first list
    Node* current = head1;
    while (current->next != nullptr) {
        current = current->next;
    }

    // Link the last node of list1 to the head of list2
    current->next = head2;
}

// Utility function to print the list
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

int main() {
    // Create first list: 10 -> 20 -> 30 -> NULL
    Node* list1 = new Node(10);
    list1->next = new Node(20);
    list1->next->next = new Node(30);

    // Create second list: 40 -> 50 -> NULL
    Node* list2 = new Node(40);
    list2->next = new Node(50);

    cout << "List 1: ";
    printList(list1);
    cout << "List 2: ";
    printList(list2);

    // Concatenate list2 to the end of list1
    concatenate(list1, list2);

    cout << "Concatenated List: ";
    printList(list1); // Output: 10 -> 20 -> 30 -> 40 -> 50 -> NULL

    return 0;
}