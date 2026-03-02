c
Node* temp = head; // Create a temporary pointer
while (temp != NULL) {
    printf("%d -> ", temp->data); // Process the data (print it)
    temp = temp->next;          // Move to the next node
}
printf("NULL\n");