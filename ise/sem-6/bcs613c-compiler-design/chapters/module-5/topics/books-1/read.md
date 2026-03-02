c
        // Original Code
        int a = 5;
        int b = a * 10; // 'a' is a constant 5
        // After Propagation
        int b = 5 * 10; // Now this can be folded
        // After Folding
        int b = 50;