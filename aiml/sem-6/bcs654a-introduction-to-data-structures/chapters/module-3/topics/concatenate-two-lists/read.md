c
// Pseudocode for integer arrays
int* concatenate(int arr1[], int size1, int arr2[], int size2) {
    int newSize = size1 + size2;
    int *newArray = (int*)malloc(newSize * sizeof(int)); // Step 2

    // Step 3: Copy first array
    for (int i = 0; i < size1; i++) {
        newArray[i] = arr1[i];
    }
    // Step 4: Append second array
    for (int i = 0; i < size2; i++) {
        newArray[size1 + i] = arr2[i];
    }
    return newArray; // Returns a new list [a1, a2, ..., b1, b2, ...]
}