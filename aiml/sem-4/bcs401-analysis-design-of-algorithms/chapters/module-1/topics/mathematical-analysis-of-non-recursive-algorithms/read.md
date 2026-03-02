python
max_val = A[0]           # 1 assignment
for i in range(1, n):    # executes n-1 times
    if A[i] > max_val:   # 1 comparison each iteration (basic operation)
        max_val = A[i]   # (assignment, happens at most n-1 times)
return max_val           # 1 operation