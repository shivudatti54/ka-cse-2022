c
// Precomputation (done once)
int precomputedFact[101];
precomputedFact[0] = 1;
for (int i = 1; i <= 100; i++) {
precomputedFact[i] = i \* precomputedFact[i-1];
}

    // Usage (extremely fast)
    int result = precomputedFact[7]; // O(1) time
