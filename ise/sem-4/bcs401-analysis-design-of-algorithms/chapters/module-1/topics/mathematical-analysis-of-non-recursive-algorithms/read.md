python
max_val = A[0]          # 1 assignment
for i in range(1, n):   # loops n-1 times
    if A[i] > max_val:  # Basic Operation: comparison
        max_val = A[i]  # (This happens only sometimes)
return max_val