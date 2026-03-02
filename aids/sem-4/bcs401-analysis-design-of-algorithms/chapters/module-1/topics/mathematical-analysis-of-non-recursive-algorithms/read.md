python
max = A[0]                 # 1 assignment
for i in 1 to n-1:         # runs n-1 times
    if A[i] > max:         # 1 comparison per iteration
        max = A[i]         # (worst-case: assignment every time)
return max                 # 1 operation