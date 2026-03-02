python
for i in range(n):        # O(n)
    for j in range(i, n): # O(n) for worst-case
        print(i, j)