java
// Inefficient - calculates array.length in every iteration
for (int i = 0; i < array.length; i++) {
// ...
}

    // Efficient - calculates length once
    int length = array.length;
    for (int i = 0; i < length; i++) {
        // ...
    }
