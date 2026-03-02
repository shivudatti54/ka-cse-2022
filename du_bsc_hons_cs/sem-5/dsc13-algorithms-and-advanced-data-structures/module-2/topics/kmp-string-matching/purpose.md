# Learning Objectives

After studying this topic, you should be able to:

1. Explain the limitations of brute-force string matching and why it leads to O(n×m) complexity in the worst case
2. Describe the core intuition behind the KMP algorithm and how it achieves linear time complexity
3. Compute the failure function (π array / LPS array) for any given pattern
4. Trace through the KMP search algorithm step-by-step to find pattern occurrences in a text
5. Analyze the time and space complexity of both the preprocessing and search phases of KMP
6. Identify real-world applications where KMP is preferred over other string matching algorithms
7. Compare KMP with other string matching algorithms like Boyer-Moore and Rabin-Karp
8. Handle edge cases in KMP including overlapping patterns and patterns with no occurrence